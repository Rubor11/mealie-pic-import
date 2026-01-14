def normalize_schema_to_mealie(schema):
    instructions = []
    for step in schema.get("recipeInstructions", []):
        if isinstance(step, dict) and "text" in step:
            instructions.append(step["text"])
        elif isinstance(step, str):
            instructions.append(step)

    ingredients = schema.get("recipeIngredient", [])

    return {
        "name": schema.get("name", "Sin nombre"),
        "description": schema.get("description", ""),
        "recipeIngredient": ingredients,
        "recipeInstructions": instructions,
        "tags": [t.strip() for t in schema.get("keywords", "").split(",") if t.strip()],
        "yield": schema.get("recipeYield", "")
    }