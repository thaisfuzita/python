#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid = dark_spell_allowed_ingredients()
    test = (ingredients.lower().split(", "))
    items = [item.capitalize() for item in test if item in valid]
    if items:
        result = ", ".join(items)
        return (f"{result} - VALID")
    return ("INVALID")
