from abc import ABC, abstractmethod


class WeaponBehaviour(ABC):

    @abstractmethod
    def useWeapon(self):
        pass


class KnifeBehaviour(WeaponBehaviour):
    def useWeapon(self):
        print("Chop chop")


class AxeBehaviour(WeaponBehaviour):
    def useWeapon(self):
        print("split split")


class BowAndArrowBehaviour(WeaponBehaviour):
    def useWeapon(self):
        print("Arjuna idhigo Bhanam Adhigo Pitta guruchusi kottu")


class SwordBehaviour(WeaponBehaviour):
    def useWeapon(self):
        print("Magadheera")
