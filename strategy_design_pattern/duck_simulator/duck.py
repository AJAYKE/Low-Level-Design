from abc import ABC, abstractmethod

from strategy_design_pattern.duck_simulator.fly_behaviour import FlyBehaviour
from strategy_design_pattern.duck_simulator.quak_behaviour import QuackBehaviour


class Duck(ABC):
    def __init__(self):
        self.fly_behaviour: FlyBehaviour = None
        self.quack_behaviour: QuackBehaviour = None

    @abstractmethod
    def display():
        pass

    def swim(self):
        print("All ducks swimssss, even decoysss")

    def perform_fly(self):
        return self.fly_behaviour.fly()

    def perform_quack(self):
        return self.quack_behaviour.quack()

    def set_new_fly_behaviour(self, fb: FlyBehaviour):
        self.fly_behaviour = fb

    def set_new_quak_behaviour(self, qb: QuackBehaviour):
        self.quack_behaviour = qb
