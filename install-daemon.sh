#!/bin/bash
# Quick installer for voice daemon

set -e

echo "🎤 Voice-to-Keyboard Daemon Installer"
echo "======================================"
echo ""

# Check if running on a system with audio
if ! [ -e /dev/snd ] && ! arecord -l &>/dev/null; then
    echo "⚠️  WARNING: No audio devices detected!"
    echo "   This system may not have a microphone."
    echo "   The daemon requires audio input to work."
    echo ""
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Install system dependencies
echo "📦 Installing system dependencies..."
if command -v apt-get &> /dev/null; then
    sudo apt update
    sudo apt install -y portaudio19-dev python3-dev python3-venv xdotool
elif command -v pacman &> /dev/null; then
    sudo pacman -S --noconfirm portaudio python xdotool
elif command -v brew &> /dev/null; then
    brew install portaudio xdotool
else
    echo "❌ Unsupported package manager. Install manually:"
    echo "   - portaudio19-dev"
    echo "   - python3-dev"
    echo "   - xdotool"
    exit 1
fi

# Create virtual environment
echo ""
echo "🐍 Setting up Python environment..."
python3 -m venv venv

# Install Python packages
echo "📚 Installing Python packages..."
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt

echo ""
echo "✅ Installation complete!"
echo ""
echo "🚀 Quick start:"
echo "   ./voice-daemon start    # Start the daemon"
echo "   ./voice-daemon status   # Check status"
echo "   ./voice-daemon stop     # Stop the daemon"
echo ""
echo "📖 Full documentation: cat DAEMON.md"
echo ""
