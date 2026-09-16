#!/usr/bin/env python3

from .. import potions
from elements import create_fire
from ..elements import create_air


def lead_to_gold() -> str:
    return(
        f"Recipe transmuting Lead to Gold: "
        f"brew '{create_air()}' and '{potions.strength_potion()}' "
        f"mixed with '{create_fire()}'"
    )
