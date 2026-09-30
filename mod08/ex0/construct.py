import sys
import os
import site


def running_venv() -> bool:
    return sys.prefix != sys.base_prefix


def show_current_env() -> None:
    current_path = sys.executable
    if running_venv():
        venv_name = os.path.basename(sys.prefix)
        site_packages = site.getsitepackages()
        env_path = sys.prefix
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {current_path}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {env_path}\n")
        print(
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n"
        )
        print("Package installation path:")
        for path in site_packages:
            print(path)
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {current_path}")
        print("Virtual Environment: None detected\n")
        print(
            "WARNING: You're in the global environment!\n"
            "The machines can see everything you install.\n"
        )
        print(
            "To enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\activate # On Windows\n"
        )
        print("Then run this program again.")


def main() -> None:
    show_current_env()


if __name__ == "__main__":
    main()
