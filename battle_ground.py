"""
random is used for coin flip, accuracy and move choice
hokemon used for testing functions
json used to load in types.json
time used to sleep script for one second
"""
import json
from time import sleep
from random import randint, random, choice
from hokemon import Hokemon


class BattleFunctions():
    """
    Used as a utility for battle_ground.py
    """
    def __init__(self, ):
        self.types_weaknesses = json.load(open("types.json"))
        self.types = list(self.types_weaknesses.keys())

    @staticmethod
    def speed_check(speed_0, speed_1):
        """
        checking who goes first based on speed
        if the speed stats are equal, then it goes down to a coing flip
        """
        if speed_0["speed"] > speed_1["speed"]:
            first_turn = 0
        elif speed_0["speed"] < speed_1["speed"]:
            first_turn = 1
        else:
            first_turn = randint(0, 1)

        return first_turn

    def weakness_calc(self, type_0, type_1):
        """
        returns a modifyer (m)
        this is always relative to hokemon_0
        so hokemon_1 modifier is 1/m

        Not very effective: x0.5
        Regulary effective: x1
        Super effective: x2
        """
        if type_0 in self.types_weaknesses.get(type_1):
            #hokemon_1 is weak to hokemon_0
            return 2
        elif type_1 in self.types_weaknesses.get(type_0):
            #hokemon_0 is weak to hokemon_1
            return 0.5
        else:
            #hokemon same types
            return 1

    @staticmethod
    def move_choice(moves):
        """
        randomly select move from move list
        """
        return choice(list(moves.keys()))

    @staticmethod
    def damage_calc(mod, move, attack_points):
        """
        mod: modifier for the attack (relative to HM0)
        move: array of move [damage, accuracy]
        health: current health of opposing hokemon

        returns the damage of attack
        """

        if round(random(), 2) > move[1]:
            return None

        return (move[0] * mod) + attack_points

if __name__ == "__main__":
    HM = [(Hokemon(), "Pikachu"), (Hokemon(), "Bulbasaur")]
    BG = BattleFunctions()

    HM[0][0].print_stats(HM[0][1])
    print("\n")
    HM[1][0].print_stats(HM[1][1])

    print("*"*100)

    TURN = 1

    sleep(15)

    while True:

        print("*"*100)

        if (TURN%2) != 0:
            HOKEMON0 = HM[0]
            HOKEMON1 = HM[1]
        else:
            HOKEMON0 = HM[1]
            HOKEMON1 = HM[0]

        MOVENAME = BG.move_choice(HOKEMON0[0].getter_stats()['moves'])
        MOVESTATS = HOKEMON0[0].getter_stats()['moves'][MOVENAME]

        WEAKNESS = BG.weakness_calc(
            HOKEMON0[0].getter_stats()['type'],
            HOKEMON1[0].getter_stats()['type']
        )

        CURRENTHEALTH = HOKEMON1[0].getter_stats()["health"]

        if WEAKNESS == 2:
            ATTACK = "super effective"
        elif WEAKNESS == 0.5:
            ATTACK = "not very effective"
        else:
            ATTACK = None

        DAMAGE = BG.damage_calc(
            WEAKNESS,
            MOVESTATS,
            HOKEMON0[0].getter_stats()["attack"]
        )

        if DAMAGE is None:
            print(f"{HOKEMON0[1]}'s attack did not hit!")
            continue

        if HOKEMON1[0].check_dead(DAMAGE) == 1:
            print(f"\n\n\n{HOKEMON1[1]} died!\n\n\n")
            break

        HOKEMON1[0].getter_stats()["health"] -= DAMAGE

        XP = HOKEMON0[0].xp_gain(DAMAGE)

        print(f"{HOKEMON0[1]} hit {HOKEMON1[1]} with {MOVENAME} for {DAMAGE}.")

        if ATTACK is not None:
            print(f"It was {ATTACK}")

        print(f"{HOKEMON1[1]} now has a health of {CURRENTHEALTH - DAMAGE}.")


        if XP[1] is True:
            print(f"\n\n{HOKEMON0[1]} leveled up!")
            HOKEMON0[0].print_stats(HOKEMON0[1])
            print(f"\n\n\n")
        else:
            print(f"{HOKEMON0[1]} gain {XP[0]} xp and now has\
 {HOKEMON0[0].getter_stats()['xp']} total xp.")

        print("*"*100)
        print("\n\n")

        sleep(5)
        TURN += 1
