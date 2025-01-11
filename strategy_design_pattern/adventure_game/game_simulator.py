from strategy_design_pattern.adventure_game.character import King
from strategy_design_pattern.adventure_game.weapon_behaviour import KnifeBehaviour

if __name__ == "__main__":
    character = King()
    character.fight()
    character.set_weapon_behaviour(KnifeBehaviour())
    character.fight()
