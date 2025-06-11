import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yt_dlp
import threading
import os
from pathlib import Path

class VideoDownloader:
    def __init__(self):
        # Ana pencere
        self.root = tk.Tk()
        self.root.title("Video İndirici 📺")
        self.root.geometry("650x550")
        self.root.resizable(True, True)
        
        # Modern görünüm için stil
        self.style = ttk.Style()
        try:
            self.style.theme_use('vista')  # Windows için modern tema
        except:
            self.style.theme_use('clam')  # Alternatif tema
        
        # Değişkenler
        self.download_path = tk.StringVar(value=str(Path.home() / "Downloads"))
        self.quality = tk.StringVar(value="best")
        self.format_type = tk.StringVar(value="mp4")
        self.is_downloading = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Ana frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Başlık
        title_label = tk.Label(
            main_frame, 
            text="🎬 Video İndirici", 
            font=("Arial", 20, "bold"),
            fg="#2563eb"
        )
        title_label.pack(pady=(0, 30))
        
        # URL girişi
        url_frame = ttk.LabelFrame(main_frame, text="Video URL'si", padding="15")
        url_frame.pack(fill="x", pady=(0, 20))
        
        self.url_entry = tk.Text(
            url_frame, 
            height=3,
            wrap=tk.WORD,
            font=("Arial", 10),
            relief="solid",
            borderwidth=1
        )
        self.url_entry.pack(fill="x", pady=(5, 0))
        self.url_entry.insert("1.0", "YouTube, Instagram, TikTok veya diğer video linkini buraya yapıştır...")
        self.url_entry.bind("<FocusIn>", self.clear_placeholder)
        
        # Kalite ve format seçimi
        options_frame = ttk.LabelFrame(main_frame, text="İndirme Seçenekleri", padding="15")
        options_frame.pack(fill="x", pady=(0, 20))
        
        # Kalite seçimi
        quality_label = ttk.Label(options_frame, text="Video Kalitesi:")
        quality_label.grid(row=0, column=0, sticky="w", padx=(0, 20), pady=(0, 5))
        
        quality_combo = ttk.Combobox(
            options_frame,
            values=["best", "1080p", "720p", "480p", "360p", "worst"],
            textvariable=self.quality,
            state="readonly",
            width=15
        )
        quality_combo.grid(row=1, column=0, sticky="w", padx=(0, 20), pady=(0, 10))
        
        # Format seçimi
        format_label = ttk.Label(options_frame, text="Format:")
        format_label.grid(row=0, column=1, sticky="w", pady=(0, 5))
        
        format_combo = ttk.Combobox(
            options_frame,
            values=["mp4", "webm", "mkv", "mp3", "m4a"],
            textvariable=self.format_type,
            state="readonly",
            width=15
        )
        format_combo.grid(row=1, column=1, sticky="w", pady=(0, 10))
        
        # İndirme yolu seçimi
        path_frame = ttk.LabelFrame(main_frame, text="İndirme Klasörü", padding="15")
        path_frame.pack(fill="x", pady=(0, 20))
        
        path_select_frame = ttk.Frame(path_frame)
        path_select_frame.pack(fill="x", pady=(5, 0))
        
        self.path_entry = ttk.Entry(
            path_select_frame,
            textvariable=self.download_path,
            state="readonly",
            font=("Arial", 9)
        )
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        path_button = ttk.Button(
            path_select_frame,
            text="Klasör Seç",
            command=self.select_download_path
        )
        path_button.pack(side="right")
        
        # İlerleme çubuğu
        progress_frame = ttk.LabelFrame(main_frame, text="İndirme Durumu", padding="15")
        progress_frame.pack(fill="x", pady=(0, 20))
        
        self.progress_label = ttk.Label(progress_frame, text="Hazır", font=("Arial", 10))
        self.progress_label.pack(pady=(0, 10))
        
        self.progress_bar = ttk.Progressbar(
            progress_frame, 
            mode='determinate',
            length=400
        )
        self.progress_bar.pack(fill="x", pady=(0, 5))
        
        # İndirme butonu
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x")
        
        self.download_button = tk.Button(
            button_frame,
            text="📥 İndir",
            command=self.start_download,
            font=("Arial", 14, "bold"),
            bg="#2563eb",
            fg="white",
            height=2,
            cursor="hand2",
            relief="flat",
            borderwidth=0
        )
        self.download_button.pack(fill="x")
        
        # Hover efektleri
        self.download_button.bind("<Enter>", lambda e: self.download_button.config(bg="#1d4ed8"))
        self.download_button.bind("<Leave>", lambda e: self.download_button.config(bg="#2563eb"))
        
    def clear_placeholder(self, event):
        if self.url_entry.get("1.0", "end-1c") == "YouTube, Instagram, TikTok veya diğer video linkini buraya yapıştır...":
            self.url_entry.delete("1.0", tk.END)
    
    def select_download_path(self):
        folder = filedialog.askdirectory(initialdir=self.download_path.get())
        if folder:
            self.download_path.set(folder)
    
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            try:
                # İlerleme yüzdesini hesapla
                if 'total_bytes' in d:
                    percent = d['downloaded_bytes'] / d['total_bytes']
                elif 'total_bytes_estimate' in d:
                    percent = d['downloaded_bytes'] / d['total_bytes_estimate']
                else:
                    percent = 0
                
                # UI güncelleme
                self.root.after(0, lambda: self.update_progress(percent, d))
                
            except Exception as e:
                print(f"Progress error: {e}")
                
        elif d['status'] == 'finished':
            self.root.after(0, lambda: self.download_finished(d['filename']))
    
    def update_progress(self, percent, d):
        self.progress_bar['value'] = percent * 100
        
        speed = d.get('speed', 0)
        if speed:
            speed_str = f"{speed/1024/1024:.1f} MB/s"
        else:
            speed_str = "Hesaplanıyor..."
            
        self.progress_label.config(text=f"İndiriliyor... %{percent*100:.1f} - {speed_str}")
    
    def download_finished(self, filename):
        self.progress_bar['value'] = 100
        self.progress_label.config(text="✅ İndirme tamamlandı!")
        self.download_button.config(text="📥 İndir", state="normal", bg="#2563eb")
        self.is_downloading = False
        
        messagebox.showinfo("Başarılı", f"Video başarıyla indirildi!\n{os.path.basename(filename)}")
    
    def start_download(self):
        url = self.url_entry.get("1.0", "end-1c").strip()
        
        if not url or url == "YouTube, Instagram, TikTok veya diğer video linkini buraya yapıştır...":
            messagebox.showerror("Hata", "Lütfen bir video URL'si girin!")
            return
        
        if self.is_downloading:
            messagebox.showwarning("Uyarı", "Zaten bir indirme işlemi devam ediyor!")
            return
        
        # UI durumunu güncelle
        self.is_downloading = True
        self.download_button.config(text="İndiriliyor...", state="disabled", bg="#6b7280")
        self.progress_bar['value'] = 0
        self.progress_label.config(text="Başlatılıyor...")
        
        # Arka planda indirme işlemini başlat
        download_thread = threading.Thread(target=self.download_video, args=(url,))
        download_thread.daemon = True
        download_thread.start()
    
    def download_video(self, url):
        try:
            # Format seçimi
            if self.format_type.get() in ['mp3', 'm4a']:
                # Sadece ses
                format_selector = 'bestaudio/best'
                outtmpl = os.path.join(self.download_path.get(), '%(title)s.%(ext)s')
            else:
                # Video
                if self.quality.get() == "best":
                    format_selector = f'best[ext={self.format_type.get()}]/best'
                elif self.quality.get() == "worst":
                    format_selector = f'worst[ext={self.format_type.get()}]/worst'
                else:
                    height = self.quality.get().replace('p', '')
                    format_selector = f'best[height<={height}][ext={self.format_type.get()}]/best[height<={height}]/best'
                
                outtmpl = os.path.join(self.download_path.get(), '%(title)s.%(ext)s')
            
            # yt-dlp konfigürasyonu
            ydl_opts = {
                'format': format_selector,
                'outtmpl': outtmpl,
                'progress_hooks': [self.progress_hook],
                'no_warnings': False,
                'extractaudio': self.format_type.get() in ['mp3', 'm4a'],
                'audioformat': self.format_type.get() if self.format_type.get() in ['mp3', 'm4a'] else None,
            }
            
            # İndirme işlemi
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
        except Exception as e:
            error_msg = str(e)
            self.root.after(0, lambda: self.download_error(error_msg))
    
    def download_error(self, error_msg):
        self.progress_bar['value'] = 0
        self.progress_label.config(text="❌ İndirme başarısız!")
        self.download_button.config(text="📥 İndir", state="normal", bg="#2563eb")
        self.is_downloading = False
        
        messagebox.showerror("İndirme Hatası", f"Video indirilemedi:\n\n{error_msg}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = VideoDownloader()
    app.run() 