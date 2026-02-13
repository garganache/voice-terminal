# Voice-to-Keyboard Daemon 🎤⌨️

**A background daemon that listens to your voice and types text directly into your terminal.**

## What It Does

1. Runs silently in the background
2. Continuously listens to your microphone
3. Transcribes speech to text
4. **Types the text into your active terminal window** (simulates keyboard)
5. No GUI, no printing - just pure typing

## Prerequisites

### Install xdotool (keyboard simulation)

**Ubuntu/Debian:**
```bash
sudo apt install xdotool
```

**Arch:**
```bash
sudo pacman -S xdotool
```

**macOS:**
```bash
brew install xdotool
```

**Wayland users:** Install `ydotool` instead:
```bash
sudo apt install ydotool
```

### System dependencies (if not already installed)

```bash
sudo apt install portaudio19-dev python3-dev python3-venv
```

## Quick Start

### 1. Install Python dependencies

```bash
cd voice-terminal
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

### 2. Start the daemon

```bash
./voice-daemon start
```

Output:
```
✅ Daemon started (PID 12345)
📝 Logs: /tmp/voice-daemon.log
🛑 Stop: voice-daemon stop
```

### 3. Speak!

- Open any terminal
- Click in the terminal window (make it active)
- **Speak into your microphone**
- Watch your words appear as if you're typing! ⌨️

### 4. Stop the daemon

```bash
./voice-daemon stop
```

## Commands

```bash
./voice-daemon start      # Start in background
./voice-daemon stop       # Stop the daemon
./voice-daemon status     # Check if running + view logs
./voice-daemon restart    # Restart the daemon
```

## How It Works

```
🎤 You speak
    ↓
🔊 Microphone captures audio
    ↓
☁️ Google Speech API transcribes
    ↓
⌨️ xdotool types text into active window
    ↓
✍️ Text appears in your terminal!
```

## Features

✅ **Silent operation** - No console output, runs in background  
✅ **Continuous listening** - Always ready for voice input  
✅ **Direct typing** - Text appears where your cursor is  
✅ **Daemon control** - Start/stop/status commands  
✅ **Logging** - All activity logged to `/tmp/voice-daemon.log`  
✅ **Works anywhere** - Types into any active window  

## Use Cases

- **Hands-free terminal input** - Code, write, command without typing
- **Accessibility** - Voice control for terminal work
- **Fast note-taking** - Speak notes into vim/nano/any editor
- **SSH sessions** - Control remote terminals by voice
- **Coding by voice** - Dictate code into your editor

## Logs

View daemon activity:

```bash
tail -f /tmp/voice-daemon.log
```

Check what was typed:
```bash
cat /tmp/voice-daemon.log | grep "Typed:"
```

## Troubleshooting

### "xdotool not found"

Install xdotool:
```bash
sudo apt install xdotool
```

### "No Default Input Device"

Your system has no microphone. The daemon needs audio input hardware.

Check available devices:
```bash
arecord -l
```

### Daemon won't start

Check logs:
```bash
cat /tmp/voice-daemon.log
```

Kill stale processes:
```bash
rm /tmp/voice-daemon.pid
./voice-daemon start
```

### Text appears in wrong window

Make sure your **terminal is the active (focused) window** before speaking.

### Wayland compatibility

If xdotool doesn't work (Wayland), install ydotool:
```bash
sudo apt install ydotool
```

The daemon will auto-detect and use it.

## Advanced: Auto-start on Login

### systemd user service

Create `~/.config/systemd/user/voice-daemon.service`:

```ini
[Unit]
Description=Voice to Keyboard Daemon
After=sound.target

[Service]
Type=forking
ExecStart=/path/to/voice-terminal/voice-daemon start
ExecStop=/path/to/voice-terminal/voice-daemon stop
PIDFile=/tmp/voice-daemon.pid
Restart=on-failure

[Install]
WantedBy=default.target
```

Enable and start:
```bash
systemctl --user enable voice-daemon
systemctl --user start voice-daemon
```

## Security Note

⚠️ **This daemon types text into your active window.** Make sure you trust the environment and understand that anything you say will be typed where your cursor is.

## Tips

- **Pause before speaking** - Give the daemon a moment to listen
- **Speak clearly** - Better recognition accuracy
- **Short phrases** - Break long text into sentences
- **Check cursor position** - Make sure you're typing where you want!

---

**Enjoy hands-free terminal input!** 🎤⌨️
