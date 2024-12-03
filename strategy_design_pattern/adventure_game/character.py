from abc import ABC

from strategy_design_pattern.adventure_game.weapon_behaviour import (
    AxeBehaviour, BowAndArrowBehaviour, KnifeBehaviour, SwordBehaviour,
    WeaponBehaviour)


class Character(ABC):
    def __init__(self):
        self.weapon_behaviour: WeaponBehaviour = None
    
    def set_weapon_behaviour(self, wb:WeaponBehaviour):
        self.weapon_behaviour = wb
    
    def fight(self):
        self.weapon_behaviour.useWeapon()


class King(Character):
    def __init__(self):
        self.weapon_behaviour = SwordBehaviour()

class Queen(Character):
    def __init__(self):
        self.weapon_behaviour = KnifeBehaviour()

class Knight(Character):
    def __init__(self):
        self.weapon_behaviour = BowAndArrowBehaviour()

class Troll(Character):
    def __init__(self):
        self.weapon_behaviour = AxeBehaviour()