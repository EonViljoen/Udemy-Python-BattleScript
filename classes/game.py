import random

# for colors apparently
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, defc, mg, items):
        # Initializing variables
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.defc = defc
        self.mg = mg
        self.items = items
        self.ac = ("Attack", "Magic", "Item")

    # Damage Methods
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0

        return self.hp

    def reduce_mp(self, cost):
        self.mp -= cost

    # Accessor Methods
    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    # Select Action
    def action_choice(self):
        i = 1

        print("Actions:")

        for item in self.ac:
            print("    ",str(i) + ":", item)
            i += 1

    # Restore Methods
    def heal(self, dmg):
        self.hp += dmg

        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def restore(self, dmg):
        self.mp += dmg

        if self.mp > self.maxmp:
            self.mp = self.maxmp

    # Select Magic and Item
    def magic_choice(self):
        i = 1

        print(bcolors.OKGREEN + bcolors.BOLD + "Magic:" + bcolors.ENDC)

        # for loop fetches item from array which contained object at each item, requiring you to name field
        for item in self.mg:
            print("    ", str(i) + ":",  item.name, "Cost: ", item.cost)

            i += 1

    def item_choice(self):
        i = 1

        print(bcolors.OKGREEN + bcolors.BOLD + "Items:" + bcolors.ENDC)

        # for loop fetches item from array which contained object at each item, requiring you to name field
        for item in self.items:
            print("    ", str(i) + ":", item["item"].name, ":", item["item"].desc, "(", item["quantity"], "Left )")

            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    " + str(i) + ". ", enemy.name)
                i += 1

        choice = int(input("Choose Target:"))-1
        return choice

    def heal_target(self, players):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "TARGET:" + bcolors.ENDC)
        for player in players:
            if player.get_hp() != 0:
                print("    " + str(i) + ". ", player.name)
                i += 1

        choice = int(input("Choose Target:"))-1
        return choice


    # Enemy Stats
    def get_enemy_stats(self):
        # Filling up bars with blocks and empty spaces
        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 100 / 2

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        # Adding white spaces to HP and MP for spacing
        # Should do this for player name as well
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        chp = ""

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        cmp = ""

        if len(hp_string) < 9:
            hp_decreased = 9 - len(hp_string)

            while hp_decreased > 0:
                chp += " "
                hp_decreased -= 1

            chp += hp_string
        else:
            chp = hp_string

        if len(mp_string) < 7:
            mp_decreased = 7 - len(mp_string)

            while mp_decreased > 0:
                cmp += " "
                mp_decreased -= 1

            cmp += mp_string
        else:
            cmp = mp_string

        print("                 __________________________________________________           __________")
        print(bcolors.BOLD + str(self.name) + ": " + chp + "|"
              + bcolors.FAIL + hp_bar + bcolors.ENDC + "|  "
              + cmp + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    # Player Stats
    def get_stats(self):
        # Filling up bars with blocks and empty spaces
        # Need to do this for top bar
        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
             mp_bar += " "

        # Adding white spaces to HP and MP for spacing
        # Should do this for player name as well
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        chp = ""

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        cmp = ""

        if len(hp_string) < 9:
            hp_decreased = 9 - len(hp_string)

            while hp_decreased > 0:
                chp += " "
                hp_decreased -= 1

            chp += hp_string
        else:
            chp = hp_string

        if len(mp_string) < 7:
            mp_decreased = 7 - len(mp_string)

            while mp_decreased > 0:
                cmp += " "
                mp_decreased -= 1

            cmp += mp_string
        else:
            cmp = mp_string

        print("                  _________________________           __________")
        print(bcolors.BOLD + str(self.name) + ": " + chp + "|"
              + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|  "
              + cmp + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def choose_enemy_magic(self):
        magic_choice = random.randrange(0, len(self.mg))
        spell = self.mg[magic_choice]
        magic_dmg = spell.generate_spell_dmg()


        pct = (self.hp / self.maxhp) * 100

        if self.mp < spell.cost or spell.type == "White" and pct > 50:
            return
            self.choose_enemy_magic()
        else:
            return spell, magic_dmg