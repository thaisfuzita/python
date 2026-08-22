class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height, verbose=False)
        self.set_age(age, verbose=False)

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height: float, verbose: bool = True) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            if verbose:
                print(f"Height updated: {int(self._height)}cm")

    def set_age(self, age: int, verbose: bool = True) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            if verbose:
                print(f"Age updated: {int(self._age)} days")

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    plant.show()
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-1)
    plant.set_age(-1)
    print()
    print("Current state: ", end="")
    plant.show()

if __name__ == "__main__":
    ft_garden_security()
