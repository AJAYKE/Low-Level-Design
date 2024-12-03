
from strategy_design_pattern.duck_simulator.duck import Duck
from strategy_design_pattern.duck_simulator.fly_behaviour import FlyWithWings
from strategy_design_pattern.duck_simulator.quak_behaviour import Quack


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behaviour = FlyWithWings()
        self.quack_behaviour = Quack()
    
    def display(self):
        print("Yohhh am visible hereee")