import alchemy.grimoire


print("=== Kaboom 0 ===")
print("Using grimoire module directly")
ingredients = "Earth, wind and fire"
print(f"Testing record light spell: {alchemy.grimoire.light_spellbook.light_spell_record('Fantasy', ingredients)}")
