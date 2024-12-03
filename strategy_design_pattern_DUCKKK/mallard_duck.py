from strategy_design_pattern_DUCKKK.duck import Duck
from strategy_design_pattern_DUCKKK.fly_behaviour import FlyWithWings
from strategy_design_pattern_DUCKKK.quak_behaviour import Quack


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behaviour = FlyWithWings()
        self.quack_behaviour = Quack()
    
    def display(self):
        print("Yohhh am visible hereee")