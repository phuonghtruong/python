#!/usr/bin/env python3.6

class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True

class Knight(Warrior):

    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7

def fight(unit_1, unit_2):
    units = [unit_1, unit_2]
    while unit_1.is_alive and unit_2.is_alive :
        for i in range(2):
            units[1-i].health -= units[i].attack
            if units[1-i].health < 0:
                units[1-i].is_alive = False
                if i:
                    return False
                else:
                    return True

if __name__ == '__main__':

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    print(fight(chuck, bruce))
    print(fight(dave, carl))
    print(chuck.is_alive)
    print(bruce.is_alive)
    print(carl.is_alive)
    print(dave.is_alive)
    print(fight(carl, mark))
    print(carl.is_alive)

