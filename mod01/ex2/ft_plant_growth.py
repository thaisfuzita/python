class Plant:
    def __init__(self, name: str, height: float, age_days: int, growth: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth = growth

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age_days} days old")

def ft_plant_growth() -> None:
    plant = Plant("Rose", 25.0, 30, 0.8)
    initial_height = plant.height
    print("=== Garden Plant Growth ===")
    plant.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()
    total_growth = round(plant.height - initial_height, 1)
    print(f"Growth this week: {total_growth}")

if __name__ == "__main__":
    ft_plant_growth()
