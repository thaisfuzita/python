import ex0.factory as f
from . import creatures


class HealingCreatureFactory(f.CreatureFactory):
    def create_base(self) -> creatures.Sproutling:
        return creatures.Sproutling()

    def create_evolved(self) -> creatures.Bloomelle:
        return creatures.Bloomelle()


class TransformCreatureFactory(f.CreatureFactory):
    def create_base(self) -> creatures.Shiftling:
        return creatures.Shiftling()

    def create_evolved(self) -> creatures.Morphagon:
        return creatures.Morphagon()
