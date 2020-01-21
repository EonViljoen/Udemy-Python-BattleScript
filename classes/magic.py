import random


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_spell_dmg(self):
        low = self.dmg - 20
        high = self.dmg + 20

        return random.randrange(low, high)

