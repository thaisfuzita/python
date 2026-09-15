def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from . import light_validator
    result = light_validator.validate_ingredients(ingredients)
    if result != "INVALID":
        return(
            f"Spell recorded: {spell_name} " 
            f"({result}) "
        )
    return (f"Spell rejected: {result}")
