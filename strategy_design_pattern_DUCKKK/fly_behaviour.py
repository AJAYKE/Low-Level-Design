from abc import ABC, abstractmethod


class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("I can fly and I am flying")


class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I cant fly, my wings doesnt work")

