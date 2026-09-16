#!/usr/bin/env python3

import random


def ft_data_alchemist() -> None:
    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
        ]

    capitalized = [name.capitalize() for name in players]
    initial_c = [
        name for name in players
        if name.capitalize() == name
    ]

    score_dict = {name: random.randint(0, 1000) for name in capitalized}

    print("=== Game Data Alchemist ===\n")

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {initial_c}\n")

    print(f"Score dict: {score_dict}")
    average_score = round((sum(score_dict.values()) / len(score_dict)), 2)
    print(f"Score average is {average_score}")
    high_scores = {
        name: score for name, score in score_dict.items()
        if score > average_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
