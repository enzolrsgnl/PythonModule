from alchemy.grimoire import record_spell
from alchemy.grimoire import validate_ingredients


def curse_breaker() -> None:
    print("Testing ingredient validation:")
    validation = validate_ingredients("fire air")
    print("validate_ingredients(\"fire air\"): " + validation)
    validation = validate_ingredients("dragon scales")
    print("validate_ingredients(\"dragon scales\"): " + validation)
    print()

    print("Testing spell recording with validation:")
    recording_validation = record_spell("Fireball", "fire air")
    print("record_spell(\"Fireball\", \"fire air\"): " + recording_validation)
    recording_validation = record_spell("Dark Magic", "shadow")
    print("record_spell(\"Dark Magic\", \"shadow\"): " + recording_validation)
    print()

    print("Testing late import technique:")
    recording_validation = record_spell("Lightning", "air")
    print("record_spell(\"Lightning\", \"air\"): " + recording_validation)


if __name__ == "__main__":
    print()
    print("=== Circular Curse Breaking ===")
    print()

    curse_breaker()
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
