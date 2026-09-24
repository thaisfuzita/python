from abc import ABC, abstractmethod
import ex0.creatures
import ex1.creatures


class BattleError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: ex0.creatures.Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: ex0.creatures.Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: ex0.creatures.Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())

    def is_valid(self, creature: ex0.creatures.Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: ex0.creatures.Creature) -> None:
        if not isinstance(creature, ex1.creatures.TransformCapability):
            raise BattleError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature: ex0.creatures.Creature) -> bool:
        return (isinstance(creature, ex1.creatures.TransformCapability))


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: ex0.creatures.Creature) -> None:
        if not isinstance(creature, ex1.creatures.HealCapability):
            raise BattleError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature: ex0.creatures.Creature) -> bool:
        return (isinstance(creature, ex1.creatures.HealCapability))
