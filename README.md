# Mealie Pic Import

This project analyzes recipe images and automatically converts them into schema.org Recipe JSON format, ready to be imported into Mealie or any compatible system.

It uses Google Gemini API for OCR + semantic understanding of recipes.

---

## Requirements

* Python 3.9+
* Gemini API key

---

## Setup

```bash
git clone https://github.com/youruser/mealie-pic-import
cd mealie-pic-import
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:

```env
# MEALIE VARIABLES
MEALIE_BASE_URL = "http://100.100.100.100:XXXX"
MEALIE_API_TOKEN = <MEALIE_API_TOKEN>

# PATH RECOMMENDATION
PENDING_DIR = "/data/pics/pending"
PROCESSED_DIR = "/data/pics/processed"
ERROR_DIR = "/data/pics/error"

# GEMINI VARIABLES
GEMINI_API_KEY = <GEMINI_API_KEY>
```

---

## Usage

Put your images in the folder and run:

```bash
python main.py
```

It will return a recipe in JSON format.

---
