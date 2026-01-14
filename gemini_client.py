import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()  # Usa GEMINI_API_KEY del entorno

PROMPT = """
You are an API that extracts cooking recipes from images.
Return ONLY valid JSON following schema.org Recipe format.
No explanations, no markdown, no text outside JSON.

Schema:
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "",
  "description": "",
  "recipeIngredient": [],
  "recipeInstructions": [
    { "@type": "HowToStep", "text": "" }
  ],
  "totalTime": "",
  "prepTime": "",
  "cookTime": "",
  "recipeYield": "",
  "keywords": ""
}
"""

def extract_recipe_from_image(image_path):
    with open(image_path, "rb") as f:
        img_bytes = f.read()

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            PROMPT,
            types.Part.from_bytes(data=img_bytes, mime_type="image/png")
        ],
    )

    raw = response.text.strip()

    # Seguridad: limpiar posibles fences
    if raw.startswith("```"):
        raw = raw.split("```")[1]

    return json.loads(raw)
