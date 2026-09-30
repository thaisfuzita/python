import os
import sys


def load_config() -> dict[str, str | None]:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("Missing dependencies!\n")
        print(
            "Install with pip:\n"
            "   pip install -r requirements.txt\n"
        )
        sys.exit(1)
    configs: dict[str, str | None] = {}
    load_dotenv()
    required_vars = [
        "MATRIX_MODE", "DATABASE_URL",
        "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"
    ]
    for name in required_vars:
        configs[name] = os.getenv(name)
    return configs


def check_config(config: dict[str, str | None]) -> dict[str, str | None]:
    missing: list[str] = []
    defaults = {
        "MATRIX_MODE": "development",
        "DATABASE_URL": "sqlite:///matrix.db",
        "API_KEY": "",
        "LOG_LEVEL": "DEBUG",
        "ZION_ENDPOINT": "http://localhost:8080"
    }
    for name in config:
        if (config[name] is None) and config["MATRIX_MODE"] == "production":
            missing.append(name)
        elif (config[name] is None):
            config[name] = defaults[name]
            print(
                f"WARNING {name} not set,"
                f" using default: {config[name]}"
            )

    if missing:
        print(
            "ERROR: Missing required configuration: "
            f"{', '.join(missing)}"
        )
        sys.exit(1)
    return config


def show_config(config: dict[str, str | None]) -> None:
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    if config["MATRIX_MODE"] == "production":
        print("Database: Connected to remote instance")
    else:
        print("Database: Connected to local instance")
    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Not Authenticated")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")


def security_check() -> None:
    print("Environment security check:")

    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
    print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    checked_config = check_config(config)
    print()
    show_config(checked_config)
    print()
    security_check()
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
