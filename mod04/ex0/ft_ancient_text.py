#!/usr/bin/env python3

import sys


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file = None
    try:
        file = open(filename, "r")
        data = file.read()
        print("---\n")
        print(f"{data}")
        print("\n---")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
