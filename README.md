# Mealie Pic Import

This project analyzes recipe images and automatically converts them into schema.org Recipe JSON format, ready to be imported into Mealie or any compatible system.

It uses Google Gemini API for OCR + semantic understanding of recipes.

---

## Requirements

* Python 3.9+ or DOcker
* Gemini API key

---

## Setup

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

## Manual Python Setup

1. Clone the repository:

```bash
git clone https://github.com/youruser/mealie-pic-import
cd mealie-pic-import
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python main.py
```

Images placed in `data/pics/pending` will be processed and moved to `processed` or `error`.

---

## Docker Setup

1. Build the Docker image:

```bash
docker compose build
```

2. Run manually:

```bash
docker compose run --rm mealie-pic-import
```

3. Place your images in `data/pics/pending` and run the container to process them.

---

## Automated Docker with Cron

You can run the container automatically every few minutes using host cron:

1. Open your crontab:

```bash
crontab -e
```

2. Add a line like this (processes every 5 minutes):

```cron
*/5 * * * * cd /path/to/mealie-pic-import && docker compose run --rm mealie-pic-import >> /path/to/mealie-pic-import/cron.log 2>&1
```

This will process any new images in `data/pics/pending` without manual intervention.

---

## Folder Structure

```
data/
 └─ pics/
     ├─ pending/   # Place new images here
     ├─ processed/ # Successfully processed images
     └─ error/     # Images that failed
```

---
