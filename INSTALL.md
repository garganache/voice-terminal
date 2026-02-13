# Installation Guide

## Quick Fix for PyAudio Build Errors

If you see this error:
```
fatal error: portaudio.h: No such file or directory
```

**You need to install system dependencies FIRST, then Python packages.**

---

## Ubuntu/Debian Installation

### Step 1: Install System Dependencies

```bash
sudo apt update
sudo apt install -y portaudio19-dev python3-dev python3-venv
```

### Step 2: Create Virtual Environment

```bash
cd voice-terminal
python3 -m venv venv
```

### Step 3: Install Python Packages

```bash
./venv/bin/pip install -r requirements.txt
```

### Step 4: Run the App

**Desktop version** (requires microphone hardware):
```bash
./run.sh
```

**Web version** (works on headless servers):
```bash
./run-web.sh
```

---

## macOS Installation

### Step 1: Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 2: Install PortAudio

```bash
brew install portaudio
```

### Step 3: Create Virtual Environment & Install

```bash
cd voice-terminal
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

### Step 4: Run

```bash
./run-web.sh
```

---

## Arch Linux Installation

```bash
sudo pacman -S portaudio python-pip
cd voice-terminal
python -m venv venv
./venv/bin/pip install -r requirements.txt
./run-web.sh
```

---

## Fedora/RHEL Installation

```bash
sudo dnf install portaudio-devel python3-devel
cd voice-terminal
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./run-web.sh
```

---

## Troubleshooting

### Still getting build errors?

Try installing PyAudio separately:

**Ubuntu/Debian:**
```bash
sudo apt install python3-pyaudio
# Then create venv WITHOUT PyAudio in requirements
```

**Or use system site-packages:**
```bash
python3 -m venv venv --system-site-packages
./venv/bin/pip install SpeechRecognition Flask
```

### No microphone on server?

Use the **web version** instead:
```bash
./run-web.sh
# Open http://localhost:5000 in browser
# Browser has microphone access!
```

### Permission denied errors?

Make scripts executable:
```bash
chmod +x run.sh run-web.sh app.py web-app.py
```

---

## Verification

Check that everything installed correctly:

```bash
./venv/bin/python -c "import speech_recognition; import pyaudio; import flask; print('✅ All packages installed!')"
```

Expected output:
```
✅ All packages installed!
```

---

## Common Issues

| Error | Solution |
|-------|----------|
| `portaudio.h: No such file` | Install `portaudio19-dev` first |
| `No Default Input Device` | Use web version (`./run-web.sh`) |
| `command not found` | Run `chmod +x *.sh` |
| `ModuleNotFoundError` | Activate venv: `source venv/bin/activate` |

---

## Need Help?

1. Check you installed **system dependencies first**
2. Use **web version** if no microphone
3. Open an issue on GitHub with your error message
