# 🏥 MediAssist AI

A rule-based medical information chatbot built with **Python (Flask)** as the backend and a clean **HTML + CSS** frontend.

> ⚠️ **Disclaimer:** MediAssist AI is for **informational purposes only**. It is **not** a substitute for professional medical advice. In an emergency, call **108**.

---

## 📁 Project Structure

```
mediassist-ai/
│
├── app.py                  # Flask backend — all medical logic & API routes
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # Frontend HTML (calls the Flask API)
│
└── static/
    └── style.css           # All CSS styling
```

---

## ✨ Features

- 💬 Covers 50+ topics — symptoms, diseases, nutrition, mental health, first aid
- 🚨 Emergency detection with prominent alerts
- 🌙 Dark / Light mode toggle
- 🕓 Chat history in browser `localStorage`
- ⚡ Quick-access suggestion chips
- 🐍 Clean Python backend — easy to extend with a real AI/ML model later

---

## 🚀 How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/samdroz/mediassist-ai.git
cd mediassist-ai
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Start the Flask server**
```bash
python app.py
```

**4. Open your browser**
```
http://127.0.0.1:5000
```

---

## 🛠️ How It Works

```
User types a message
        │
        ▼
   index.html (JS)
  POST /chat  →  app.py
                   │
            Keyword matching
            against MEDICAL_DATA
                   │
            JSON response
                   │
        ◄──────────┘
   Rendered in chat UI
```

The `app.py` holds all medical knowledge and response logic. To add a new topic, simply add a new key-value pair to the `MEDICAL_DATA` dictionary.

---

## 🛠️ Built With

| Layer    | Technology         |
|----------|--------------------|
| Backend  | Python, Flask      |
| Frontend | HTML5, CSS3, Vanilla JS |
| Icons    | Font Awesome 6     |
| Fonts    | Google Fonts (Inter) |

---

## 📄 License

MIT License — open source, free to use.
