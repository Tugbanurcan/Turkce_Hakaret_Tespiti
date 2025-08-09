import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from flask import Flask, render_template, request

app = Flask(__name__)

model_path = r"C:\Users\tugba\OneDrive\Masaüstü\tasarım\model\best_model"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()

label_names = [
    "Tespit",
    "Küfür",
    "Tehdit",
    "Hakaret",
    "Dolandırıcılık",
    "Cinsel İçerik",
    "Irkçılık"
]

def predict(text, threshold=0.5):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probs = torch.sigmoid(logits).squeeze().cpu().tolist()

    # probs listesi float sayılar içeriyor, modelin kategoriye göre olasılıkları
    return probs

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    results = []
    if request.method == 'POST':
        tweet_url = request.form.get('tweet_url', '').strip()
        text_input = request.form.get('text_input', '').strip()

        # Tweet URL'den metin çekme opsiyonel, burada sadece inputlardan birini alıyoruz
        if tweet_url:
            # Burada tweet'ten metin çekme fonksiyonu yazabilirsin (isteğe bağlı)
            text = "Tweetten çekilen metin burada olacak..."
        elif text_input:
            text = text_input

        if text:
            probs = predict(text)
            results = []
            for label, prob in zip(label_names, probs):
                results.append({
                    "label": label,
                    "prob": int(prob * 100),  # yüzdeye çevir
                    "detected": prob >= 0.5  # eşik
                })

    return render_template('index.html', text=text, results=results)

if __name__ == '__main__':
    app.run(debug=True)
