import sys
import importlib
import importlib.metadata


def check_dependencies() -> bool:
    ok = True
    imports = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization"
    }
    print("Checking dependencies:")
    for package in imports:
        try:
            importlib.import_module(package)
            print(
                f"[OK] {package} ({importlib.metadata.version(package)})"
                f" - {imports[package]} ready"
            )
        except ImportError:
            print(f"[KO] {package} - {imports[package]} missing")
            ok = False
    return ok


def instructions() -> None:
    print()
    print("Missing dependencies!\n")

    print(
        "Install with pip:\n"
        "   pip install -r requirements.txt\n"
    )

    print(
        "Install with Poetry:\n"
        "   poetry install\n"
        "	poetry run python loading.py\n"
    )

    print(
        "pip: you manage the venv, simple package list\n"
        "Poetry: manages the venv for you, locks exact versions"
    )


def generate_matrix_data() -> "pd.DataFrame":  # type: ignore[name-defined]  # noqa: F821
    import numpy as np
    import pandas as pd
    rng = np.random.default_rng()
    matrix = rng.random(1000)
    df = pd.DataFrame({"data": matrix})
    return df


def plot(df: "pd.DataFrame") -> str:  # type: ignore[name-defined]  # noqa: F821
    import matplotlib.pyplot as plt

    filename = "matrix_analysis.png"
    print("Generating visualization...")
    plt.hist(df["data"])
    plt.savefig(filename)
    plt.close()
    return filename


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    if not check_dependencies():
        instructions()
        sys.exit(1)
    df = generate_matrix_data()
    print()
    print("Analyzing Matrix data...")
    print(f"Processing {len(df)} data points...")
    filename = plot(df)
    print()
    print("Analysis complete!")
    print(f"Results saved to: {filename}")


if __name__ == "__main__":
    main()
