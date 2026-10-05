#!/usr/bin/env python3

import alchemy.grimoire


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    ingredients = "Earth, wind and fire"
    spell = alchemy.grimoire.light_spellbook.light_spell_record
    print(
        f"Testing record light spell: "
        f"{spell('Fantasy', ingredients)}"
    )
