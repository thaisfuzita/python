import sys


def valid_scores(args: list[str]) -> list[int]:
    valid = []
    for arg in args:
        try:
            valid.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return valid


def analytics(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}\n")


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    valid = valid_scores(sys.argv[1:])
    if valid:
        analytics(valid)
    else:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ...\n"
        )


if __name__ == "__main__":
    ft_score_analytics()
