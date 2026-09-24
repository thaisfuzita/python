from abc import ABC, abstractmethod
import ex0.creatures as c


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(c.Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return ("Sproutling uses Vine Whip!")

    def heal(self) -> str:
        return ("Sproutling heals itself for a small amount")


class Bloomelle(c.Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return ("Bloomelle uses Petal Dance!")

    def heal(self) -> str:
        return ("Bloomelle heals itself and others for a large amount")


class Shiftling(c.Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.transformed = False

    def attack(self) -> str:
        if self.transformed:
            return ("Shiftling performs a boosted strike!")
        return ("Shiftling attacks normally.")

    def transform(self) -> str:
        self.transformed = True
        return ("Shiftling shifts into a sharper form!")

    def revert(self) -> str:
        self.transformed = False
        return ("Shiftling returns to normal.")


class Morphagon(c.Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.transformed = False

    def attack(self) -> str:
        if self.transformed:
            return ("Morphagon unleashes a devastating morph strike!")
        return ("Morphagon attacks normally.")

    def transform(self) -> str:
        self.transformed = True
        return ("Morphagon morphs into a dragonic battle form!")

    def revert(self) -> str:
        self.transformed = False
        return ("Morphagon stabilizes its form.")
