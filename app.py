#!/usr/bin/env python3
"""
Voice-to-Text Terminal App
Speak and see your words appear in the terminal in real-time.
"""

import speech_recognition as sr
import sys
import os
from datetime import datetime

class VoiceTerminal:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise on first run
        print("🎤 Calibrating microphone for ambient noise...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
        print("✓ Calibration complete!\n")
    
    def listen_and_transcribe(self, continuous=True):
        """
        Listen for speech and transcribe to terminal.
        
        Args:
            continuous: If True, keeps listening. If False, transcribes once.
        """
        print("=" * 60)
        print("🎙️  VOICE TERMINAL - Ready to listen!")
        print("=" * 60)
        print("• Speak clearly into your microphone")
        print("• Press Ctrl+C to stop\n")
        
        session_start = datetime.now()
        transcription_count = 0
        
        try:
            while True:
                print("\n🔴 Listening... (speak now)")
                
                with self.microphone as source:
                    # Listen for audio
                    audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=None)
                
                print("🔄 Processing...")
                
                try:
                    # Transcribe using Google Speech Recognition (free)
                    text = self.recognizer.recognize_google(audio)
                    
                    # Display transcription
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    transcription_count += 1
                    
                    print(f"\n┌─ [{timestamp}] Transcription #{transcription_count}")
                    print(f"│")
                    print(f"│  {text}")
                    print(f"└─")
                    
                    # Save to file
                    self.save_transcription(text, timestamp)
                    
                except sr.UnknownValueError:
                    print("❌ Could not understand audio - please speak more clearly")
                except sr.RequestError as e:
                    print(f"❌ Could not request results; {e}")
                
                if not continuous:
                    break
                    
        except KeyboardInterrupt:
            session_duration = datetime.now() - session_start
            print(f"\n\n{'=' * 60}")
            print(f"📊 Session Summary")
            print(f"{'=' * 60}")
            print(f"Duration: {session_duration}")
            print(f"Transcriptions: {transcription_count}")
            print(f"Saved to: transcriptions.txt")
            print("\n👋 Goodbye!\n")
    
    def save_transcription(self, text, timestamp):
        """Save transcription to a text file."""
        filename = "transcriptions.txt"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {text}\n")

def main():
    """Main entry point."""
    print("\n" + "=" * 60)
    print("  VOICE-TO-TEXT TERMINAL")
    print("=" * 60)
    print()
    
    # Check if microphone is available
    try:
        sr.Microphone.list_microphone_names()
    except Exception as e:
        print(f"❌ Error: Could not access microphone")
        print(f"   {e}")
        print("\nMake sure you have:")
        print("  • A microphone connected")
        print("  • portaudio19-dev installed (sudo apt install portaudio19-dev)")
        print("  • PyAudio installed (pip install pyaudio)")
        sys.exit(1)
    
    # Initialize and run
    try:
        app = VoiceTerminal()
        app.listen_and_transcribe(continuous=True)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
