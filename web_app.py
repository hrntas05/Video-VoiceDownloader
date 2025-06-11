from flask import Flask, render_template, request, jsonify, send_file
import yt_dlp
import os
import threading
from pathlib import Path
import json

app = Flask(__name__)

# Global değişkenler
download_status = {
    'status': 'ready',
    'progress': 0,
    'speed': '',
    'filename': '',
    'error': ''
}

def progress_hook(d):
    global download_status
    if d['status'] == 'downloading':
        try:
            if 'total_bytes' in d:
                percent = d['downloaded_bytes'] / d['total_bytes']
            elif 'total_bytes_estimate' in d:
                percent = d['downloaded_bytes'] / d['total_bytes_estimate']
            else:
                percent = 0
            
            speed = d.get('speed', 0)
            if speed:
                speed_str = f"{speed/1024/1024:.1f} MB/s"
            else:
                speed_str = "Hesaplanıyor..."
            
            download_status.update({
                'status': 'downloading',
                'progress': percent * 100,
                'speed': speed_str
            })
        except Exception as e:
            print(f"Progress error: {e}")
            
    elif d['status'] == 'finished':
        download_status.update({
            'status': 'finished',
            'progress': 100,
            'filename': os.path.basename(d['filename'])
        })

def download_video(url, quality, format_type, download_path):
    global download_status
    try:
        download_status['status'] = 'starting'
        
        # Format seçimi
        if format_type in ['mp3', 'm4a']:
            format_selector = 'bestaudio/best'
        else:
            if quality == "best":
                format_selector = f'best[ext={format_type}]/best'
            elif quality == "worst":
                format_selector = f'worst[ext={format_type}]/worst'
            else:
                height = quality.replace('p', '')
                format_selector = f'best[height<={height}][ext={format_type}]/best[height<={height}]/best'
        
        outtmpl = os.path.join(download_path, '%(title)s.%(ext)s')
        
        ydl_opts = {
            'format': format_selector,
            'outtmpl': outtmpl,
            'progress_hooks': [progress_hook],
            'no_warnings': False,
            'extractaudio': format_type in ['mp3', 'm4a'],
            'audioformat': format_type if format_type in ['mp3', 'm4a'] else None,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
    except Exception as e:
        download_status.update({
            'status': 'error',
            'error': str(e)
        })

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def start_download():
    global download_status
    
    if download_status['status'] == 'downloading':
        return jsonify({'error': 'Zaten bir indirme işlemi devam ediyor!'})
    
    data = request.json
    url = data.get('url', '').strip()
    quality = data.get('quality', 'best')
    format_type = data.get('format', 'mp4')
    download_path = data.get('path', str(Path.home() / "Downloads"))
    
    if not url:
        return jsonify({'error': 'Lütfen bir video URL\'si girin!'})
    
    # İndirme klasörünü oluştur
    os.makedirs(download_path, exist_ok=True)
    
    # Reset status
    download_status = {
        'status': 'ready',
        'progress': 0,
        'speed': '',
        'filename': '',
        'error': ''
    }
    
    # Arka planda indirme başlat
    thread = threading.Thread(target=download_video, args=(url, quality, format_type, download_path))
    thread.daemon = True
    thread.start()
    
    return jsonify({'success': True})

@app.route('/status')
def get_status():
    return jsonify(download_status)

if __name__ == '__main__':
    # Templates klasörünü oluştur
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, host='127.0.0.1', port=5000) 