import os
import shutil
from dotenv import load_dotenv
from gemini_client import extract_recipe_from_image
from normalizer import normalize_schema_to_mealie
from mealie_client import create_recipe

load_dotenv()

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Rutas relativas
PENDING_DIR = os.path.join(BASE_DIR, "data", "pics", "pending")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "pics", "processed")
ERROR_DIR = os.path.join(BASE_DIR, "data", "pics", "error")

def ensure_dirs():
    for d in [PENDING_DIR, PROCESSED_DIR, ERROR_DIR]:
        os.makedirs(d, exist_ok=True)

def is_image(file):
    return file.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))

def process_images():
    files = [f for f in os.listdir(PENDING_DIR) if is_image(f)]
    # print(PENDING_DIR)
    # print(files)
    if not files:
        print("No hay imágenes para procesar.")
        return

    for file in files:
        src = os.path.join(PENDING_DIR, file)
        try:
            print(f"Procesando {file}...")
            schema = extract_recipe_from_image(src)
            mealie_data = normalize_schema_to_mealie(schema)
            create_recipe(mealie_data)
            shutil.move(src, os.path.join(PROCESSED_DIR, file))
            print(f"OK: {file}")
        except Exception as e:
            print(f"ERROR {file}: {e}")
            shutil.move(src, os.path.join(ERROR_DIR, file))




if __name__ == "__main__":
    ensure_dirs()
    process_images()
