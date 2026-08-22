class Plant:
    def __init__(self, name: str, height: int, age: int, growth: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def grow(self) -> None:
        self.height += self.growth
    
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def ft_plant_factory() -> None:
    plant1 = Plant("Rose", 25.0, 30, 0.8)
    plant2 = Plant("Oak", 200.0, 365, 2.3)
    plant3 = Plant("Cactus", 5.0, 90, 1.9)
    plant4 = Plant("Sunflower", 80.0, 45, 1.2)
    plant5 = Plant("Fern", 15.0, 120, 3.2)
    garden = [plant1, plant2, plant3, plant4, plant5]
    print("=== Plant Factory Output ===")
    for plant in garden:
        print("Created: ", end="")
        plant.show()

if __name__ == "__main__":
    ft_plant_factory()
