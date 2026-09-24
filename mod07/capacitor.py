import ex1


def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = ex1.HealingCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform() -> None:
    print("Testing Creature with transform capability")
    factory = ex1.TransformCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    test_healing()
    print()
    test_transform()


if __name__ == "__main__":
    main()
