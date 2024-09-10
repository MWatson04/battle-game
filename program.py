# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from engine import *

def run():
    game_obj = Game()
    game_obj.game_setup()
    game_obj.state_transition()

    game_obj.play_game()

run()
