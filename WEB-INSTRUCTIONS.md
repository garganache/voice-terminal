# 🌐 Web Voice Terminal - SOLUTION FOR HEADLESS SERVERS

Since this Ubuntu server has **no microphone**, use this web-based version that accesses your **browser's microphone** instead.

## Quick Start

### 1. Start the web server:
```bash
cd /home/ubuntu/.openclaw/workspace/voice-terminal
./run-web.sh
```

### 2. Open in your browser:
```
http://localhost:5000
```

Or from another device on the same network:
```
http://YOUR_SERVER_IP:5000
```

## How It Works

1. **Server runs on Ubuntu** (headless, no microphone)
2. **You open browser** on your laptop/phone (has microphone)
3. **Browser captures audio** via Web API
4. **Sends to server** for transcription
5. **Displays in browser** AND prints to server terminal
6. **Saves to file** (`transcriptions.txt`)

## Using the Web Interface

1. Click the big **microphone button** 🎤
2. **Allow microphone access** when browser asks
3. **Speak clearly**
4. Click the **pause button** ⏸️ to stop
5. See your transcription appear!

## Features

✅ **Beautiful web UI** - No terminal needed  
✅ **Real-time recording** - Visual feedback  
✅ **History tracking** - See all transcriptions  
✅ **Dual output** - Browser + server terminal  
✅ **Auto-save** - Everything saved to file  
✅ **Mobile-friendly** - Works on phones/tablets  

## Accessing from Your Phone/Laptop

If you're on the same WiFi network:

```bash
# Find your server's IP
hostname -I

# Then open in browser:
http://YOUR_IP:5000
```

Example: `http://192.168.1.100:5000`

## Why This Works

- **Server has no mic** → Can't use desktop Python app
- **Browser has mic** → Web Audio API captures sound
- **Server does transcription** → Google Speech Recognition API
- **Result**: You get both browser display AND terminal output!

## Troubleshooting

### Can't access from another device?

Check firewall:
```bash
sudo ufw allow 5000
```

### Browser won't access microphone?

- Must use **HTTPS** or **localhost**
- For remote access, consider SSH tunnel:
  ```bash
  ssh -L 5000:localhost:5000 user@server
  ```
  Then open `http://localhost:5000` on your local machine

---

**Perfect solution for headless servers!** 🎉
