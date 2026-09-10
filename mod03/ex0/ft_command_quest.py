import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    total_args = len(sys.argv)

    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_args - 1}")
        for arg in range(1, total_args):
            print(f"Argument {arg}: {sys.argv[arg]}")

    print(f"Total arguments: {total_args}\n")


if __name__ == "__main__":
    ft_command_quest()
