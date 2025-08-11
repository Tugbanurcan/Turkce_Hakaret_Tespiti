"# Turkce_Hakaret_Tespiti" 

Bu proje, Türkçe metinlerde **çok-etiketli sınıflandırma** yapmak için Hugging Face Transformers ve PyTorch kullanılarak geliştirilmiş bir makine öğrenmesi modeli ve bu modeli gerçek zamanlı test edebileceğiniz **Flask tabanlı web arayüzünü** içerir.

---

## 📌 Proje Özeti
- **Model Eğitimi**
  - BERT-tabanlı (`AutoModelForSequenceClassification`) çok-etiketli sınıflandırma modeli
  - Excel formatında veri okuma ve ön işleme
  - Sınıf ağırlıkları ile `BCEWithLogitsLoss` kullanımı
  - Eğitim/validasyon/test seti ayrımı
  - Per-sınıf **optimum threshold** belirleme
  - Eğitim metriklerinin görselleştirilmesi

- **Web Arayüzü**
  - Flask ile gerçek zamanlı tahmin
  - Metin girişi veya tweet URL’si üzerinden test
  - Her etiket için olasılık (%) ve eşik üstünde olup olmadığını gösterme
  - Hazır **best_model** klasöründen yükleme

---
