from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid = light_spell_allowed_ingredients()
    items = ingredients.lower()
    if any(item in items for item in valid):
        return (f"{ingredients} - VALID")
    return ("INVALID")
