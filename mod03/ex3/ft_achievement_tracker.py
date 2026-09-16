#!/usr/bin/env python3

import random


def gen_player_achievements(achievements: set[str]) -> set[str]:
    num_items = random.randint(0, len(achievements))
    items = random.sample(list(achievements), num_items)
    return set(items)


def achievement_system() -> None:
    achievements = {
            'Crafting Genius', 'Strategist', 'World Savior',
            'Speed Runner', 'Survivor', 'Master Explorer',
            'Treasure Hunter', 'Unstoppable', 'First Steps',
            'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer'
        }

    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print(
        f"\nAll distinct achievements: "
        f"{set.union(alice, bob, charlie, dylan)}\n"
    )

    print(
        f"Common achievements: "
        f"{set.intersection(alice, bob, charlie, dylan)}\n"
    )

    print(
        f"Only Alice has: "
        f"{alice.difference(bob.union(charlie, dylan))}"
    )
    print(
        f"Only Bob has: "
        f"{bob.difference(alice.union(charlie, dylan))}"
    )
    print(
        f"Only Charlie has: "
        f"{charlie.difference(alice.union(bob, dylan))}"
    )
    print(
        f"Only Dylan has: "
        f"{dylan.difference(alice.union(bob, charlie))}\n"
    )

    print(f"Alice is missing: {set.difference(achievements, alice)}")
    print(f"Bob is missing: {set.difference(achievements, bob)}")
    print(f"Charlie is missing: {set.difference(achievements, charlie)}")
    print(f"Dylan is missing: {set.difference(achievements, dylan)}")


if __name__ == "__main__":
    achievement_system()
