#!/usr/bin/env python3

def secure_archive(
        filename: str, action: str = "r", content: str = ""
        ) -> tuple[bool, str]:
    if action not in ("r", "w"):
        return (False, "Invalid action")
    try:
        with open(filename, action) as file:
            if action == "r":
                data = file.read()
            elif action == "w":
                file.write(content)
                data = "Content successfully written to file"
    except OSError as e:
        return (False, str(e))
    return (True, data)


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")

    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    content = secure_archive("/not/existing/file", "r")
    print(content)

    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    content = secure_archive("/etc/master.passwd", "r")
    print(content)

    print()
    print("Using 'secure_archive' to read from a regular file:")
    content = secure_archive("text.txt", "r")
    print(content)

    print()
    print("Using 'secure_archive' to write content to a new file:")
    content = secure_archive(
        "text.txt", "w", "blablabla\n"
        )
    print(content)


if __name__ == "__main__":
    ft_vault_security()
