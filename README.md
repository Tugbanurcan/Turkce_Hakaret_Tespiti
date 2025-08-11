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
  - Metin girişi üzerinden test
  - Her etiket için olasılık (%) ve eşik üstünde olup olmadığını gösterme
  - Hazır **best_model** klasöründen yükleme

---


<img width="928" height="813" alt="image" src="https://github.com/user-attachments/assets/010a5b26-5dce-4595-a6e9-ec18c6e433a2" />


<img width="807" height="881" alt="image" src="https://github.com/user-attachments/assets/d34ab2d8-54af-4b74-a797-8de54910c4de" />


<img width="757" height="882" alt="image" src="https://github.com/user-attachments/assets/42a7899d-5e4d-4430-a926-439b6524c2d3" />




