from strategy_design_pattern_DUCKKK.fly_behaviour import FlyNoWay
from strategy_design_pattern_DUCKKK.mallard_duck import MallardDuck
from strategy_design_pattern_DUCKKK.quak_behaviour import Squeak

if __name__ == "__main__":
    duck = MallardDuck()
    duck.perform_fly()
    duck.display()
    duck.perform_quack()
    duck.swim()

    duck.set_new_fly_behaviour(FlyNoWay())
    duck.perform_fly()

    duck.set_new_quak_behaviour(Squeak())
    duck.perform_quack()