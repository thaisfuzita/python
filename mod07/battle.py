import ex0


def testing_factory(factory: ex0.CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: ex0.CreatureFactory,
           factory2: ex0.CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()
    print(base1.describe())
    print(" vs.")
    print(base2.describe())
    print(" fight!")
    print(base1.attack())
    print(base2.attack())


def main() -> None:
    flame = ex0.FlameFactory()
    aqua = ex0.AquaFactory()
    testing_factory(flame)
    print()
    testing_factory(aqua)
    print()
    battle(flame, aqua)


if __name__ == "__main__":
    main()
