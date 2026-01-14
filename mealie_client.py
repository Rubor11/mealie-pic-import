import os
import requests
from dotenv import load_dotenv

load_dotenv()

MEALIE_BASE_URL = os.getenv("MEALIE_BASE_URL")
MEALIE_API_TOKEN = os.getenv("MEALIE_API_TOKEN")

def create_recipe(recipe_data):
    url = f"{MEALIE_BASE_URL}/api/recipes"

    headers = {
        "Authorization": f"Bearer {MEALIE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    r = requests.post(url, headers=headers, json=recipe_data, timeout=30)

    if r.status_code not in (200, 201):
        raise Exception(f"Mealie error: {r.status_code} - {r.text}")
        return r.json()