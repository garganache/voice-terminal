#!/usr/bin/env python3
"""
Web-based Voice Terminal
Access from browser to use your computer's microphone
"""

from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
from datetime import datetime
import os
import base64
import io

app = Flask(__name__)
recognizer = sr.Recognizer()

# Store transcriptions in memory
transcriptions = []

@app.route('/')
def index():
    """Serve the web interface"""
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    """Receive audio from browser and transcribe it"""
    try:
        # Get audio data from request
        audio_data = request.files.get('audio')
        if not audio_data:
            return jsonify({'error': 'No audio data received'}), 400
        
        # Read audio file
        audio_bytes = audio_data.read()
        
        # Convert to AudioData object
        audio = sr.AudioData(audio_bytes, sample_rate=16000, sample_width=2)
        
        # Transcribe
        try:
            text = recognizer.recognize_google(audio)
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            # Store transcription
            transcription = {
                'timestamp': timestamp,
                'text': text
            }
            transcriptions.append(transcription)
            
            # Save to file
            save_transcription(text, timestamp)
            
            # Print to terminal
            print(f"\n[{timestamp}] {text}")
            
            return jsonify({
                'success': True,
                'text': text,
                'timestamp': timestamp
            })
        
        except sr.UnknownValueError:
            return jsonify({'error': 'Could not understand audio'}), 400
        except sr.RequestError as e:
            return jsonify({'error': f'Service error: {e}'}), 500
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/history')
def history():
    """Get transcription history"""
    return jsonify(transcriptions)

def save_transcription(text, timestamp):
    """Save transcription to file"""
    with open('transcriptions.txt', 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {text}\n")

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    print("\n" + "=" * 60)
    print("  WEB VOICE TERMINAL")
    print("=" * 60)
    print("\n🌐 Starting server...")
    print("\n📱 Open in your browser:")
    print("   http://localhost:5000")
    print("\n💡 Use your browser's microphone to transcribe speech")
    print("   Transcriptions appear both in browser AND terminal")
    print("\n🛑 Press Ctrl+C to stop\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
