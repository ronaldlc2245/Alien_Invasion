# Gives spaceship super speed movement for 3 moves
import time
from threading import Thread
import game_functions as gf


class Ability(Thread):

    ability_available = 0

    def __init__(self):
        Thread.__init__(self)


def run(self):
    timer = time.time()
    future = time.time() + 10

    if timer >= future and Ability.ability_available <= 2:
        Ability.ability_available

    run()




