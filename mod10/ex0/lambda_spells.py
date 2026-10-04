#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered = filter(lambda x: x['power'] >= min_power, mages)
    return list(filtered)


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        max_power = 0
        min_power = 0
        avg_power = 0.0
    else:
        max_power = max(mages, key=lambda x: x['power'])['power']
        min_power = min(mages, key=lambda x: x['power'])['power']
        powers = map(lambda x: x['power'], mages)
        avg_power = sum(powers) / len(mages)
    status = {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": round(avg_power, 2)
    }
    return status


def main() -> None:
    print()
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'relic'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
    ]

    print("Testing artifact sorter...")
    sort = artifact_sorter(artifacts)
    print(
        f"{sort[0]['name']} ({sort[0]['power']} power) comes "
        f"before {sort[1]['name']} ({sort[1]['power']} power)\n"
    )

    print("Testing spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(' '.join(transformed))


if __name__ == "__main__":
    main()
