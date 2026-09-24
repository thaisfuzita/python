import ex0
import ex1
import ex2


def battle(
        opponents: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            try:
                print("* Battle *")
                print(creature1.describe())
                print(" vs.")
                print(creature2.describe())
                print(" now fight!")
                strategy1.act(creature1)
                strategy2.act(creature2)
                print()
            except ex2.BattleError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame = ex0.FlameFactory()
    aqua = ex0.AquaFactory()
    healing = ex1.HealingCreatureFactory()
    transform = ex1.TransformCreatureFactory()
    normal = ex2.NormalStrategy()
    aggressive = ex2.AggressiveStrategy()
    defensive = ex2.DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    t0 = [(flame, normal), (healing, defensive)]
    battle(t0)

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    t1 = [(flame, aggressive), (healing, defensive)]
    battle(t1)
    print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    t2 = [
        (aqua, normal),
        (healing, defensive),
        (transform, aggressive)
    ]
    battle(t2)


if __name__ == "__main__":
    main()
