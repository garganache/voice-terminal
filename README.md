# Voice-to-Keyboard 🎤⌨️

**Speak and your words get typed into your terminal automatically.**

## Two Modes

### 🤖 Daemon Mode (Recommended)
**Background daemon that types text directly into your terminal**
- Runs silently in background
- Types where your cursor is
- No printing, just pure keyboard simulation
- See [DAEMON.md](DAEMON.md) for details

### 📺 Terminal Display Mode
**Interactive app that shows transcriptions**
- Desktop app: prints to terminal
- Web app: browser interface
- See below for details

## Quick Start

⚠️ **IMPORTANT:** Install system dependencies BEFORE Python packages!

### 1. Install System Dependencies (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install -y portaudio19-dev python3-dev python3-venv
```

**Other distros:** See [INSTALL.md](INSTALL.md) for macOS, Arch, Fedora instructions.

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Install Python Dependencies

```bash
./venv/bin/pip install -r requirements.txt
```

**If you get build errors**, you missed step 1! See [INSTALL.md](INSTALL.md) for troubleshooting.

### 4. Run the App

**Web version** (recommended for servers):
```bash
./run-web.sh
# Open http://localhost:5000 in browser
```

**Desktop version** (requires microphone):

```bash
./run.sh
```

Or directly:

```bash
./venv/bin/python app.py
```

## Usage

1. Run the app
2. Wait for "🔴 Listening... (speak now)"
3. Speak clearly into your microphone
4. See your transcription appear in the terminal
5. Press Ctrl+C to stop

## Features

- ✅ Real-time speech-to-text transcription
- ✅ Automatic ambient noise calibration
- ✅ Saves all transcriptions to `transcriptions.txt`
- ✅ Session statistics (duration, count)
- ✅ Works offline with Sphinx (optional)
- ✅ Uses Google Speech Recognition (free, requires internet)

## Troubleshooting

### "Could not access microphone"

- Check microphone is connected: `arecord -l`
- Test recording: `arecord -d 5 test.wav`
- Install portaudio: `sudo apt install portaudio19-dev`

### "ModuleNotFoundError: No module named '_portaudio'"

```bash
sudo apt install python3-pyaudio portaudio19-dev
pip install --upgrade pyaudio
```

### No internet connection?

For offline transcription, install PocketSphinx:

```bash
sudo apt install -y swig libpulse-dev
pip install pocketsphinx
```

Then modify the app to use `recognize_sphinx()` instead of `recognize_google()`.

## Requirements

- Python 3.6+
- Ubuntu/Debian Linux
- Microphone
- Internet connection (for Google Speech Recognition)

## Output

All transcriptions are saved to `transcriptions.txt` in the format:

```
[12:34:56] Hello, this is a test transcription.
[12:35:10] Another sentence spoken into the microphone.
```
