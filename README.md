# Aiva Financial Dashboard

## 📊 Finansal Analiz ve Raporlama Sistemi

Aiva Financial Dashboard, işletmeler için kapsamlı bir finansal analiz ve raporlama aracıdır. Bu uygulama, finansal verileri görselleştirme, analiz etme ve tahmin yapma özellikleri sunarak stratejik kararlar almanıza yardımcı olur.

## 🌟 Özellikler

- **Finansal Dashboard**: Satış, gider ve kar metriklerinin gerçek zamanlı görselleştirilmesi
- **Detaylı Finansal Analiz**: Satış, gider ve karlılık metrikleri için kapsamlı analizler
- **Piyasa Verileri**: Döviz kurları ve diğer piyasa göstergeleri takibi
- **Tahminler**: Makine öğrenmesi ile satış ve gider tahminleri
- **Raporlama**: Özelleştirilmiş raporlar oluşturma ve paylaşma imkanı

## 🚀 Kurulum

### Gereksinimler

- Python 3.9+
- Pip
- Git (opsiyonel)

### Adım 1: Projeyi Bilgisayarınıza İndirin

```bash
git clone https://github.com/your-username/aiva-financial.git
cd aiva-financial
```

veya ZIP olarak indirip açabilirsiniz.

### Adım 2: Sanal Ortam Oluşturun (Opsiyonel)

```bash
python -m venv venv
# Windows için
venv\Scripts\activate
# MacOS/Linux için
source venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### Adım 4: Uygulamayı Çalıştırın

```bash
streamlit run Home.py
```

## 📊 Kullanım Kılavuzu

### Veri Yükleme

1. Ana sayfada "CSV Dosyası Yükle" butonunu kullanarak finansal veri dosyanızı yükleyin
2. Desteklenen format: CSV (EBİTTA_EKİM_2022.csv gibi)
3. Veri yüklendikten sonra tüm analiz özellikleri aktif hale gelecektir

### Dashboard

- Genel finansal metriklerin özeti
- Satış, gider ve kar metriklerinin görselleştirilmesi
- Önemli içgörülerin otomatik oluşturulması

### Finansal Analiz

- **Satış Analizi**: Aylık satış trendleri ve büyüme oranları
- **Gider Analizi**: Gider kalemlerinin detaylı dökümü ve analizleri
- **Karlılık Analizi**: Kar marjı trendi ve hedeflerle karşılaştırma

### Piyasa Verileri

- Döviz kurları (USD/TRY, EUR/TRY, vb.) takibi
- BIST 100 ve diğer finansal endeksler
- Teknik göstergeler ve piyasa özeti

### Tahminler

- Makine öğrenmesi modelleri ile gelecek dönem tahminleri:
  - Satış tahmini
  - Gider tahmini
  - Kar tahmini
- Güven aralıkları ve model doğruluk metrikleri

### Raporlar

- Farklı rapor türleri:
  - Özet rapor
  - Aylık rapor
  - Gider raporu
  - Detaylı rapor
- Raporları Excel veya PDF formatında dışa aktarma
- E-posta ile rapor paylaşımı

## 📁 Proje Yapısı

```
aiva-financial/
│
├── Home.py                   # Ana sayfa
├── main.py                   # Ana uygulama dosyası
├── README.md                 # Proje açıklaması
├── requirements.txt          # Bağımlılıklar
├── setup.py                  # Proje kurulum dosyası
│
├── config/                   # Konfigürasyon dosyaları
│   ├── __init__.py
│   ├── settings.py           # Uygulama ayarları
│   └── style.py              # UI stilleri
│
├── data/                     # Örnek veri dosyaları
│   └── sample_data.csv
│
├── pages/                    # Uygulama sayfaları
│   ├── __init__.py
│   ├── 1_Dashboard.py        # Dashboard sayfası
│   ├── 2_Finansal_Analiz.py  # Finansal analiz sayfası
│   ├── 3_Piyasa_Verileri.py  # Piyasa verileri sayfası
│   ├── 4_Tahminler.py        # Tahminler sayfası
│   └── 5_Raporlar.py         # Raporlar sayfası
│
└── utils/                    # Yardımcı fonksiyonlar
    ├── __init__.py
    ├── charts.py             # Grafikler için fonksiyonlar
    ├── data_loader.py        # Veri yükleme fonksiyonları
    ├── helpers.py            # Genel yardımcı fonksiyonlar
    └── predictions.py        # Tahmin modelleri
```

## 📈 Veri Gereksinimleri

Uygulama, aşağıdaki şekilde yapılandırılmış bir CSV dosyası ile çalışmaktadır:

- **EBİTTA_EKİM_2022.csv** gibi her satırı bir gider kalemi ve her sütunu bir ayı temsil eden finansal veri tablosu
- Sütunlar: Gider kalemi, ocak, şubat, mart... aralık, genel toplam, ortalama, satış pay oranı
- Satırlar: Personel giderleri, malzeme giderleri, finansman giderleri vb.

## 🛠️ Teknik Detaylar

Aiva Financial Dashboard aşağıdaki teknolojileri kullanmaktadır:

- **Streamlit**: Web arayüzü ve interaktif dashboard
- **Pandas & NumPy**: Veri manipülasyonu ve analizi
- **Plotly**: İnteraktif veri görselleştirme
- **Scikit-learn**: Makine öğrenmesi ile tahmin modelleri
- **yfinance**: Piyasa verilerine erişim

## 🔮 Planlanan Özellikler

- Çoklu dil desteği
- Mobil uyumlu arayüz
- Daha gelişmiş tahmin modelleri
- Daha fazla veri formatı desteği
- Kullanıcı yetkilendirme sistemi
- Gerçek zamanlı veri entegrasyonları

## 🤝 Katkıda Bulunma

Projeye katkıda bulunmak isterseniz:

1. Bu depoyu forklayın
2. Yeni bir feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylı bilgi için LICENSE dosyasına bakınız.

## 📞 İletişim

Sorularınız veya önerileriniz için [email@example.com](mailto:email@example.com) adresine e-posta gönderebilirsiniz.

---

Made with ❤️ by Aiva Financial Team
