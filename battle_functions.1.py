"""
random is used for coin flip
hokemon used for testing functions
"""
from random import randint
from hokemon import Hokemon

class BattleFunctions():
    """
    Used as a utility for battle_ground.py
    """
    def __init__(self):
        self.types = ["Fire", "Water", "Grass"]


    @staticmethod
    def speed_check(speed_0, speed_1):
        """
        checking who goes first based on speed
        if the speed stats are equal, then it goes down to a coing flip
        """
        if speed_0["speed"] > speed_1["speed"]:
            first_turn = 0
        elif speed_0["speed"] < speed_1["speed"]:
            first_turn = 0
        else:
            first_turn = randint(0, 1)

        return first_turn

    def weakness_calc(self, type_0, type_1):
        """
        returns the adavantaged pokemon
        value 0: hokemon 1 has the advantage
        value 1: hokemon 2 has the advantage
        """

        if type_0 == "Grass" and type_1 == "Fire":
            return 1
        elif (self.types.index(type_0) + 1) == self.types.index(type_1):
            return 1

        if type_0 == "Fire" and type_1 == "Grass":
            return 0
        elif (self.types.index(type_0) - 1) == self.types.index(type_1):
            return 0

        return -1


if __name__ == "__main__":
    BG = BattleFunctions()
    HM0 = Hokemon()
    HM1 = Hokemon()

    print(f"Hokemon 1: {HM0.get_stats()}.\nHokemon 2: {HM1.get_stats()}.")

    print(f"\n {BG.weakness_calc(HM0.stats['type'], HM1.stats['type'])}")
