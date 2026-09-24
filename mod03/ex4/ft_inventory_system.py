#!/usr/bin/env python3

import sys


def get_items(args: list[str]) -> dict[str, int]:
    items = {}
    for arg in args:
        key_value = arg.split(":")
        if len(key_value) != 2:
            print(f"Error - invalid parameter '{key_value[0]}'")
            continue

        key, value = key_value
        if key in items:
            print(f"Redundant item '{key_value[0]}' - discarding")
            continue

        try:
            items[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
            continue

    return items


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    items = get_items(args)
    if not items:
        print("Got inventory: {}")
        return
    print(f"Got inventory: {items}")
    print(f"Item list: {list(items.keys())}")
    total = sum(items.values())
    print(f"Total quantity of the {len(items)}: {total}")
    first = list(items)[0]
    value_max = first
    value_min = first
    for item in items:
        print(
            f"Item {item} represents "
            f"{round((items[item] / total) * 100, 1)}%"
        )
        if items[item] > items[value_max]:
            value_max = item
        if items[item] < items[value_min]:
            value_min = item
    print(f"Item most abundant: {value_max} with quantity {items[value_max]}")
    print(f"Item least abundant: {value_min} with quantity {items[value_min]}")

    items.update({"magic_item": 1})
    print(f"Updated inventory: {items}")


if __name__ == "__main__":
    ft_inventory_system()
