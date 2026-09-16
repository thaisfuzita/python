#!/usr/bin/env python3

import math


def get_position() -> tuple[float, float, float]:
    while True:
        valid = []
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
            )
        coordinates = user_input.split(",")
        if len(coordinates) != 3:
            print("Invalid syntax")
            continue
        for i in coordinates:
            try:
                valid.append(float(i))
            except ValueError as e:
                print(f"Error on parameter '{i}': {e}")
                break

        if len(valid) == 3:
            x, y, z = valid
            return (x, y, z)


def get_distance(
        p1: tuple[float, float, float],
        p2: tuple[float, float, float] = (0, 0, 0)) -> float:

    distance = math.sqrt(
        (p2[0] - p1[0])**2 +
        (p2[1] - p1[1])**2 +
        (p2[2] - p1[2])**2
    )
    return round(distance, 4)


def get_player_pos() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    p1 = get_position()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    print(f"Distance to center: {get_distance(p1)}\n")

    print("Get a second set of coordinates")
    p2 = get_position()
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{get_distance(p1, p2)}"
    )


if __name__ == "__main__":
    get_player_pos()
