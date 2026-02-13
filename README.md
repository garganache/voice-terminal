# Voice-to-Text Terminal 🎤

A simple Python app that lets you speak and see your words transcribed in real-time in the terminal.

## Quick Start

### 1. Install System Dependencies (Ubuntu)

```bash
sudo apt update
sudo apt install -y portaudio19-dev python3-pyaudio
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install SpeechRecognition PyAudio
```

### 3. Run the App

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
