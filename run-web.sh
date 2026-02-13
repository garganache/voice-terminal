#!/bin/bash
# Web Voice Terminal Launcher

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Run: python3 -m venv venv && ./venv/bin/pip install -r requirements.txt"
    exit 1
fi

echo "🌐 Starting Web Voice Terminal..."
echo ""
echo "📱 Open in your browser:"
echo "   http://localhost:5000"
echo ""
echo "💡 If accessing from another device on your network:"
echo "   http://$(hostname -I | awk '{print $1}'):5000"
echo ""

./venv/bin/python web-app.py
