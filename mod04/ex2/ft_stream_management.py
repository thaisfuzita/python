import sys


def read_data(filename: str) -> list[str] | None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    file = None
    data = ""
    try:
        file = open(filename, "r")
        data = file.read()
        print("---\n")
        print(f"{data}")
        print("\n---")
    except OSError as e:
        sys.stdout.flush()
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        return None
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")
    return data.splitlines()


def transform_data(lines: list[str]) -> list[str]:
    new_data = [f"{line}#" for line in lines]

    print("Transform data:")
    print("---\n")
    for line in new_data:
        print(line)
    print("\n---")
    return new_data


def save_file(filename: str, data: list[str]) -> None:
    print(f"Saving data to '{filename}'")
    file = None
    try:
        file = open(filename, "w")
        for line in data:
            file.write(line + "\n")
    except OSError as e:
        sys.stdout.flush()
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        return
    finally:
        if file is not None:
            file.close()
    print(f"Data saved in file '{filename}'.")


def ft_stream_management() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]
    lines = read_data(filename)
    if lines is None:
        return
    new_data = transform_data(lines)
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_file = sys.stdin.readline()
    if new_file.endswith("\n"):
        new_file = new_file[:-1]
    if not new_file:
        print("Not saving data.")
        return
    save_file(new_file, new_data)


if __name__ == "__main__":
    ft_stream_management()
