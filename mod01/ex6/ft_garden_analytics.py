class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Status: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self._stats = self._Stats()

    def grow(self, size: float) -> None:
        self.height += size
        self._stats.record_grow()

    def age_up(self, days: int) -> None:
        self.age += days
        self._stats.record_age()

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

    def show_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self, verbose: bool = True) -> None:
        if verbose:
            print(f"[asking the {self.name} to grow and bloom]")
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.blooming:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        print(f"[make {self.name} grow, age and bloom]")
        super().bloom(verbose = False)
        self.age_up(20)
        self.grow(30)
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")
        
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.record_shade()
        print(f"[asking the {self.name} to produce shade]")
        print(f"The {self.name.capitalize()} now produces a shade of {self.height:.1f}cm long "
              f"and {self.trunk_diameter:.1f}cm wide")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.show_stats()

def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    flower = Flower("rose", 15.0, 10, "red")
    flower.show()
    display_stats(flower)
    flower.grow(8)
    flower.bloom()
    flower.show()
    display_stats(flower)
    print()

    print("=== Tree")
    tree = Tree("oak", 200.0, 365, 5.0)
    tree.show()
    display_stats(tree)
    tree.produce_shade()
    display_stats(tree)
    print()

    print("=== Seed")
    seed = Seed("sunflower", 80.0, 45, "yellow")
    seed.show()
    seed.bloom()
    seed.show()
    display_stats(seed)
    print()

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_stats(anon)

if __name__ == "__main__":
    ft_garden_analytics()
