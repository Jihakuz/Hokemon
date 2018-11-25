"""
random used for stat generation
json used to get types.json and moves.json
pprint used to make dictionary printing look nicer
"""
from random import randint
from pprint import pprint
import json

class Hokemon():
    """
    Holds all infomation about hokemon
    """
    def __init__(self):
        """
        When calculating weakness, index n is weak to index (n+1),
        and vise versa with strength
        """

        self.types = list(json.load(open("types.json")).keys())
        self.moves = json.load(open("moves.json"))

        self.lvlup = None

        self.stats = {
            "attack": randint(0, 10),
            "defence": randint(0, 10),
            "speed": randint(0, 10),
            "health": randint(450, 500),
            "xp": 0,
            "lvl": "1",
            "type": self.types[randint(0, (len(self.types)-1))],
        }

        self.get_moves()


    def print_stats(self, name):
        """
        A nicer way of printing hokemon's stats

        name: simply used to print out hokemon's name with its stats
        """
        print(f"{name}'s stats are:\n")
        pprint(self.stats)

    def getter_stats(self):
        """
        Returns stats of hokemon.
        """
        return self.stats

    def get_moves(self):
        """
        Initilises moves and also updates them on level up.
        """

        self.stats["moves"] = self.moves[self.stats["lvl"]][self.stats["type"]]

    def xp_gain(self, damage):
        """
        Controls the amount of xp gain from one hit
        and if the pokemon should level up

        damage: used to work out experience gain
        """
        self.stats["xp"] = self.stats["xp"] + round((damage * 0.25), 0)


        if ((self.stats["xp"]) > (int(self.stats["lvl"]) * 50)) and (int(self.stats["lvl"]) != 3):
            self.level_up((self.stats["xp"]) - (int(self.stats["lvl"]) * 50))
            self.lvlup = True
        else:
            self.lvlup = False

        return (round((damage * 0.25), 0), self.lvlup)

    def level_up(self, extra_xp):
        """
        Used to level up hokemon

        extra_xp: xp that goes over the top of the max xp for that level
        """
        self.stats["xp"] = extra_xp
        self.stats["lvl"] = str(int(self.stats["lvl"]) + 1)
        self.stats["attack"] += randint(1, 3)
        self.stats["defence"] += randint(1, 3)
        self.get_moves()


    def check_dead(self, damage):
        """
        Checks if hokemon is dead

        1: is dead
        0: is not dead
        """
        if (self.stats["health"]- damage) <= 0:
            return 1
        else:
            return 0



if __name__ == "__main__":
    PIKACHU = Hokemon()
    pprint(PIKACHU.getter_stats())
