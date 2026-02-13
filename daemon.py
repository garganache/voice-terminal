#!/usr/bin/env python3
"""
Voice-to-Keyboard Daemon
Runs in background, listens to voice, types text into active window
"""

import speech_recognition as sr
import subprocess
import os
import signal
import sys
import time
from datetime import datetime

class VoiceDaemon:
    def __init__(self, pidfile='/tmp/voice-daemon.pid', logfile='/tmp/voice-daemon.log'):
        self.pidfile = pidfile
        self.logfile = logfile
        self.recognizer = sr.Recognizer()
        self.running = True
        
    def log(self, message):
        """Write to log file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.logfile, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")
    
    def type_text(self, text):
        """Type text using xdotool (simulates keyboard input)"""
        try:
            # Use xdotool to type text into active window
            # Add a space after each phrase for natural dictation
            subprocess.run(['xdotool', 'type', '--', text + ' '], check=True)
            self.log(f"Typed: {text}")
        except subprocess.CalledProcessError:
            self.log("ERROR: xdotool failed")
        except FileNotFoundError:
            # Try ydotool for Wayland
            try:
                subprocess.run(['ydotool', 'type', text + ' '], check=True)
                self.log(f"Typed (ydotool): {text}")
            except:
                self.log("ERROR: Neither xdotool nor ydotool available")
    
    def listen_and_type(self):
        """Main daemon loop: listen -> transcribe -> type"""
        with sr.Microphone() as source:
            self.log("Daemon started - adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            self.log("Ready - listening for voice input...")
            
            while self.running:
                try:
                    # Listen for audio
                    audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=None)
                    
                    # Transcribe
                    try:
                        text = self.recognizer.recognize_google(audio)
                        
                        # Type the text into active window
                        self.type_text(text)
                        
                    except sr.UnknownValueError:
                        # Couldn't understand - just skip silently
                        pass
                    except sr.RequestError as e:
                        self.log(f"API error: {e}")
                        time.sleep(5)  # Wait before retrying
                        
                except KeyboardInterrupt:
                    break
                except Exception as e:
                    self.log(f"Error: {e}")
                    time.sleep(1)
    
    def start(self):
        """Start the daemon"""
        # Check if already running
        if os.path.exists(self.pidfile):
            with open(self.pidfile, 'r') as f:
                pid = int(f.read().strip())
            try:
                os.kill(pid, 0)  # Check if process exists
                print(f"Daemon already running (PID {pid})")
                sys.exit(1)
            except OSError:
                # Stale pidfile
                os.remove(self.pidfile)
        
        # Fork to background
        try:
            pid = os.fork()
            if pid > 0:
                # Parent process
                print(f"✅ Daemon started (PID {pid})")
                print(f"📝 Logs: {self.logfile}")
                print(f"🛑 Stop: voice-daemon stop")
                sys.exit(0)
        except OSError as e:
            print(f"Fork failed: {e}")
            sys.exit(1)
        
        # Child process (daemon)
        os.setsid()
        os.chdir('/')
        os.umask(0)
        
        # Write PID file
        with open(self.pidfile, 'w') as f:
            f.write(str(os.getpid()))
        
        # Redirect stdout/stderr
        sys.stdout.flush()
        sys.stderr.flush()
        
        with open('/dev/null', 'r') as devnull:
            os.dup2(devnull.fileno(), sys.stdin.fileno())
        with open(self.logfile, 'a') as f:
            os.dup2(f.fileno(), sys.stdout.fileno())
            os.dup2(f.fileno(), sys.stderr.fileno())
        
        # Setup signal handlers
        signal.signal(signal.SIGTERM, self._signal_handler)
        signal.signal(signal.SIGINT, self._signal_handler)
        
        # Run the daemon
        try:
            self.listen_and_type()
        finally:
            self._cleanup()
    
    def stop(self):
        """Stop the daemon"""
        if not os.path.exists(self.pidfile):
            print("Daemon not running")
            return
        
        with open(self.pidfile, 'r') as f:
            pid = int(f.read().strip())
        
        try:
            os.kill(pid, signal.SIGTERM)
            print(f"✅ Daemon stopped (PID {pid})")
        except OSError:
            print("Daemon not running (stale pidfile)")
        
        self._cleanup()
    
    def status(self):
        """Check daemon status"""
        if not os.path.exists(self.pidfile):
            print("❌ Daemon not running")
            return
        
        with open(self.pidfile, 'r') as f:
            pid = int(f.read().strip())
        
        try:
            os.kill(pid, 0)
            print(f"✅ Daemon running (PID {pid})")
            print(f"📝 Logs: {self.logfile}")
            
            # Show last 5 log lines
            if os.path.exists(self.logfile):
                print("\n📋 Recent activity:")
                subprocess.run(['tail', '-n', '5', self.logfile])
        except OSError:
            print("❌ Daemon not running (stale pidfile)")
            self._cleanup()
    
    def _signal_handler(self, signum, frame):
        """Handle termination signals"""
        self.log(f"Received signal {signum}, shutting down...")
        self.running = False
    
    def _cleanup(self):
        """Clean up PID file"""
        if os.path.exists(self.pidfile):
            os.remove(self.pidfile)

def main():
    daemon = VoiceDaemon()
    
    if len(sys.argv) < 2:
        print("Usage: daemon.py {start|stop|status|restart}")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'start':
        daemon.start()
    elif command == 'stop':
        daemon.stop()
    elif command == 'status':
        daemon.status()
    elif command == 'restart':
        daemon.stop()
        time.sleep(1)
        daemon.start()
    else:
        print(f"Unknown command: {command}")
        print("Usage: daemon.py {start|stop|status|restart}")
        sys.exit(1)

if __name__ == '__main__':
    main()
