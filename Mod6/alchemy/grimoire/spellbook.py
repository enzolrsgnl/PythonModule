def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire.validator import validate_ingredients
    status = validate_ingredients(ingredients)
    if status == ingredients + " - VALID":
        return "Spell recorded: " + spell_name + " (" + status + ")"
    else:
        return "Spell rejected: " + spell_name + " (" + status + ")"
