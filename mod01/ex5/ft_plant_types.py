class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.blooming:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, 
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of {self.height:.1f}cm long"
            f" and {self.trunk_diameter:.1f}cm wide.")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm wide.")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, 
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow_age(self, size: float, days: int) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        self.height += size * days
        self.age += days
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")

def ft_plant_types() -> None:
    flower = Flower("rose", 15.0, 10, "red")
    tree = Tree("oak", 200.0, 365, 5.0)
    vegetable = Vegetable("tomato", 5.0, 10, "april")

    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower.show()
    flower.bloom()
    flower.show()
    print()

    print("=== Tree")
    tree.show()
    tree.produce_shade()
    print()

    print("=== Vegetable")
    vegetable.show()
    vegetable.grow_age(2.1, 20)
    vegetable.show()

if __name__ == "__main__":
    ft_plant_types()
