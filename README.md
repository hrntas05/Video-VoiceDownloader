# 🎬 Video İndirici

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Modern ve kullanıcı dostu video indirici uygulaması**  
*YouTube, Instagram, TikTok ve 1000+ platformdan video indirin*

</div>

---

## 📋 İçindekiler

- [✨ Özellikler](#-özellikler)
- [🌟 Versiyon Seçimi](#-versiyon-seçimi)
- [🚀 Hızlı Başlangıç](#-hızlı-başlangıç)
- [🎯 Kullanım Kılavuzu](#-kullanım-kılavuzu)
- [🛠️ Desteklenen Platformlar](#️-desteklenen-platformlar)
- [📁 Proje Yapısı](#-proje-yapısı)
- [🐛 Sorun Giderme](#-sorun-giderme)
- [📞 Destek](#-destek)

---

## ✨ Özellikler

### 🎥 **Platform Desteği**
- **1000+ Site**: YouTube, Instagram, TikTok, Twitter, Facebook, Vimeo ve daha fazlası
- **Geniş Format**: Video (MP4, WebM, MKV) ve Ses (MP3, M4A) formatları

### 🎛️ **Kalite Seçenekleri**
- **Ultra HD**: 4K, 1080p (Full HD), 720p (HD)
- **Standart**: 480p, 360p kalite seçenekleri
- **Otomatik**: En iyi kalite otomatik seçimi

### 📊 **Gelişmiş Özellikler**
- **Gerçek Zamanlı İzleme**: İndirme ilerlemesi ve hız göstergesi
- **Çoklu Arayüz**: Web ve masaüstü versiyonları
- **Responsive Tasarım**: Mobil ve masaüstü uyumlu
- **Özelleştirilebilir**: İndirme klasörü seçimi

---

## 🌟 Versiyon Seçimi

<table>
<tr>
<td width="50%">

### 🌐 **Web Uygulaması** *(Önerilen)*

```bash
python web_app.py
```

**✅ Avantajları:**
- Platform bağımsız çalışır
- Modern gradient tasarım
- Tcl/Tk sorunları yok
- Mobil uyumlu arayüz
- Tarayıcıda çalışır

**📍 Erişim:** `http://127.0.0.1:5000`

</td>
<td width="50%">

### 🖥️ **Masaüstü Uygulaması**(web surumu tavsiyemdir)

```bash
py main.py
```

**⚠️ Notlar:**
- Tkinter tabanlı GUI
- Windows/Linux uyumlu
- Tcl/Tk gerektirir
- Yerel uygulama deneyimi

**🔧 Sorun Durumunda:** Web versiyonunu kullanın

</td>
</tr>
</table>

---

## 🚀 Hızlı Başlangıç

### 📋 **Gereksinimler**
- **Python**: 3.7 veya üstü ([İndir](https://python.org))
- **İnternet**: Aktif bağlantı
- **Disk**: İndirmeler için yeterli alan

### ⚡ **Kurulum**

```bash
# 1. Depoyu klonlayın
git clone https://github.com/kullanici/video-indirici.git
cd video-indirici

# 2. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 3. Uygulamayı başlatın
py web_app.py    # Web versiyonu (önerilen)
# VEYA
py main.py       # Masaüstü versiyonu
```

### 🎉 **İlk Kullanım**
1. Tarayıcınızda `http://127.0.0.1:5000` adresine gidin
2. Video linkini yapıştırın
3. Kalite ve formatı seçin
4. **İndir** butonuna tıklayın!

---

## 🎯 Kullanım Kılavuzu

### 📱 **Adım Adım Kullanım**

| Adım | İşlem | Açıklama |
|------|-------|----------|
| **1** | 🔗 **URL Girişi** | Video linkini text alanına yapıştırın |
| **2** | 🎛️ **Kalite Seçimi** | İstenilen video kalitesini seçin |
| **3** | 📁 **Format Seçimi** | Video (MP4, WebM) veya Ses (MP3, M4A) |
| **4** | 📂 **Klasör Belirleme** | İndirme konumunu seçin |
| **5** | 📥 **İndirme** | İndir butonuna tıklayın ve bekleyin |

### 🎨 **Arayüz Özellikleri**

- **🎯 Modern Tasarım**: Gradient arka plan ve temiz layout
- **📊 İlerleme Çubuğu**: Gerçek zamanlı indirme durumu
- **⚡ Hız Göstergesi**: MB/s cinsinden indirme hızı
- **✅ Durum Bildirimleri**: Başarı ve hata mesajları
- **📱 Responsive**: Tüm cihazlarda uyumlu

---

## 🛠️ Desteklenen Platformlar

<div align="center">

### 🎬 **Video Platformları**

| Platform | Durum | Platform | Durum |
|----------|-------|----------|-------|
| 📺 YouTube | ✅ | 📸 Instagram | ✅ |
| 🎵 TikTok | ✅ | 🐦 Twitter | ✅ |
| 👥 Facebook | ✅ | 🎬 Vimeo | ✅ |
| 📺 DailyMotion | ✅ | 🎯 Twitch | ✅ |

*Ve 1000+ diğer platform...*

</div>

---

## 📁 Proje Yapısı

```
video-indirici/
├── 📄 README.md              # Bu dosya
├── 📄 requirements.txt       # Python bağımlılıkları
├── 🌐 web_app.py             # Flask web uygulaması
├── 🖥️ main.py                # Tkinter masaüstü uygulaması
└── 📁 templates/
    └── 🎨 index.html         # Web arayüzü template
```

### 📦 **Bağımlılıklar**

```
yt-dlp>=2023.12.30     # Video indirme motoru
Flask>=2.3.0           # Web framework
Pillow>=10.1.0         # Görüntü işleme
requests>=2.31.0       # HTTP istekleri
```

---

## 🐛 Sorun Giderme

### ❌ **Yaygın Hatalar ve Çözümleri**

<details>
<summary><strong>🔧 ModuleNotFoundError</strong></summary>

**Problem:** Python modülü bulunamıyor  
**Çözüm:**
```bash
pip install -r requirements.txt
```
</details>

<details>
<summary><strong>🔧 Tcl/Tk Hatası</strong></summary>

**Problem:** "Tcl wasn't installed properly"  
**Çözüm:** Web versiyonunu kullanın:
```bash
python web_app.py
```
</details>

<details>
<summary><strong>🔧 İndirme Hatası</strong></summary>

**Problem:** Video indirilemedi  
**Çözümler:**
- URL'nin doğru olduğunu kontrol edin
- İnternet bağlantınızı kontrol edin
- yt-dlp'yi güncelleyin: `pip install --upgrade yt-dlp`
</details>

<details>
<summary><strong>🔧 Yavaş İndirme</strong></summary>

**Problem:** İndirme hızı çok yavaş  
**Çözümler:**
- İnternet bağlantınızı kontrol edin
- Daha düşük kalite seçin
- Farklı bir zaman diliminde deneyin
</details>

### ⚠️ **Önemli Notlar**

- Bazı videolar telif hakkı nedeniyle indirilemeyebilir
- Instagram ve TikTok için hesap giriş gerekebilir
- Büyük dosyalar için yeterli disk alanı bulundurun
- Web versiyonu tüm işletim sistemlerinde çalışır

---

## 🔄 Güncellemeler

### 📈 **Düzenli Güncelleme**

```bash
# yt-dlp güncelleme (önemli!)
pip install --upgrade yt-dlp

# Tüm paketleri güncelleme
pip install --upgrade -r requirements.txt
```

### 📅 **Sürüm Geçmişi**

- **v2.0**: Web uygulaması eklendi
- **v1.5**: Modern UI tasarımı
- **v1.0**: İlk kararlı sürüm

---

## 📞 Destek

<div align="center">

### 🤝 **Yardım Almak**

**🌐 Web Versiyonu Önerilir** *(En Kararlı)*

| Sorun Türü | İletişim Yolu |

| 📧 **Genel Destek** | [E-posta](harun.tas0501@gmail.com) |

### ⭐ **Projeyi Beğendiyseniz**

Bu projeyi faydalı bulduysanız ⭐ vermeyi unutmayın!

</div>

---

<div align="center">

**MIT License** | Made with ❤️ | **Python** 🐍


</div>

