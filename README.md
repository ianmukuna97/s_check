# 🛡️ Scam Detector

A web application built with **Python** and **Django** that helps users identify and flag potential scams — including suspicious messages and emails — using machine learning and rule-based detection techniques.

---

## ✨ Features

- 🔍 **Text & Message Analysis** — Scans messages for scam indicators and suspicious patterns
- 📧 **Email Detection** — Flags phishing and fraudulent emails
- 📊 **Risk Score** — Returns a confidence/risk score for each submission
- 🗂️ **Scan History** — Keeps a log of all previous scans
- 🔐 **User Authentication** — Register, log in, and manage your scan history

---

## 🧰 Tech Stack

| Layer      | Technology                    |
|------------|-------------------------------|
| Backend    | Python 3.x, Django            |
| Database   | SQLite (dev) / PostgreSQL (prod) |
| Frontend   | HTML, CSS, Bootstrap          |
| ML/NLP     | scikit-learn / NLTK (if used) |
| Auth       | Django built-in auth          |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/scam-detector.git
   cd scam-detector
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```env
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** _(optional, for admin panel)_

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your browser.

---

## 📁 Project Structure

```
scam-detector/
├── detector/                   # Main app (views, models, logic)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── analyzer.py         # Scam detection logic
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── scam_detector/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── manage.py
└── README.md
```

---

## 🔌 API Endpoints

| Method | Endpoint              | Description                        |
|--------|-----------------------|------------------------------------|
| POST   | `/api/scan/text/`     | Analyze a text message for scams   |
| POST   | `/api/scan/email/`    | Detect phishing in an email        |
| GET    | `/api/history/`       | Get scan history for logged-in user|

### Example Request

```bash
curl -X POST http://127.0.0.1:8000/api/scan/text/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Congratulations! You have won a $1000 gift card. Click here to claim."}'
```

### Example Response

```json
{
  "input": "Congratulations! You have won a $1000 gift card...",
  "is_scam": true,
  "confidence": 0.94,
  "reason": "Contains known scam phrases and urgency patterns"
}
```

---

## ⚙️ Configuration

You can customize detection sensitivity and rules in `detector/analyzer.py`:

```python
SCAM_KEYWORDS = ["you have won", "claim your prize", "verify your account", ...]
RISK_THRESHOLD = 0.7  # Scores above this are flagged as scams
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please make sure your code follows PEP 8 style guidelines and includes tests where applicable.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/ianmukuna97)
- Email: ianmukuna.dev@gmail.com

---

## 🙏 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [scikit-learn](https://scikit-learn.org/)
- [NLTK](https://www.nltk.org/)
