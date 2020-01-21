import random

from classes.magic import Spell
from classes.game import Person, bcolors
from classes.inventory import Item

# Create save system?

# Black Spell List
fire = Spell("Fireball", 20, 500, "Black")
thunder = Spell("Thunderbolt", 20, 550, "Black")
blizzard = Spell("Blizzard", 10, 450, "Black")
deathray = Spell("Doom", 50, 2000, "Black")
acid = Spell("Acid Splash", 10, 300, "Black")
quake = Spell("Earthquake", 30, 700, "Black")

# White Spell List
heal = Spell("Heal", 20, 500, "White")
gHeal = Spell("Great Heal", 50, 1000, "White")
light = Spell("Holy Light", 30, 750, "White")

# Item List
potion = Item("Potion", "Potion", "Heals 50 HP", 500)
gpotion = Item("Great Potion", "Potion", "Heals 200 HP", 2000)
spotion = Item("Super Potion", "Potion", "Heals 500 HP", 5000)
elixir = Item("Elixir", "Elixir", "Restores HP/MP", 9999)
helixir = Item("High Elixir", "Elixir", "Restores HP/MP of Party", 9999)
bomb = Item("Bomb", "Attack", "Deals 500 Damage", 1000)

# Player Spells
player_spells = [fire, thunder, blizzard, heal, gHeal, quake]

# Enemy Spells
enemy_spells = [fire, thunder, blizzard, acid, quake, heal]

# Player Items
player_items = [{"item": potion, "quantity": 5},
                {"item": gpotion, "quantity": 3},
                {"item": spotion, "quantity": 1},
                {"item": elixir, "quantity": 3},
                {"item": helixir, "quantity": 1},
                {"item": bomb, "quantity": 3}]

# Player Person
player1 = Person("Bale  ", 3500, 150, 60, 30, player_spells, player_items)
player2 = Person("Thern ", 4500, 200, 60, 30, player_spells, player_items)
player3 = Person("Jax   ", 3000, 100, 60, 30, player_spells, player_items)


enemy1 = Person("Orc  ", 5000, 50, 1000, 25, enemy_spells, [])
enemy2 = Person("Troll", 2000, 50, 300, 25, enemy_spells, [])
enemy3 = Person("Imp  ", 500, 50, 50, 25, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

defeated_enemies = 0
defeated_heroes = 0

run = True

# Battling
while run:
    # Stats
    # print(bcolors.OKGREEN + "\nHP:", player.get_hp(), "/", player.get_maxhp(), bcolors.ENDC)
    # print(bcolors.OKBLUE + "MP:", player.get_mp(), "/", player.get_maxmp(), bcolors.ENDC)

    print("\nName              HP                                  MP")
    for player in players:
        # Get Player Stats
        player.get_stats()
    print("____________________________________")

    for enemy in enemies:
        # Get Enemy Stats
        enemy.get_enemy_stats()

    print("____________________________________")

    for player in players:
        if player.get_hp() != 0:
            # Choose Action for each player
            print("\n" + bcolors.BOLD + player.name + ":" + bcolors.ENDC)
            print("====================================")
            player.action_choice()
            choice = input("\nChoose Action:")
            action = int(choice) - 1
            print("____________________________________")

            # If Attacking
            if action == 0:
                # Choose Enemy. Damage Generation and HP reduction
                dmg = player.generate_damage()
                target = player.choose_target(enemies)
                enemies[target].take_dmg(dmg)

                # String Output
                print("\nAttacked", enemies[target].name, "for", dmg)
                print("____________________________________")

                # Remove enemy from attacking list
                if enemies[target].get_hp() == 0:
                    print("\n", enemies[target].name, "is Dead")
                    print("____________________________________")
                    del enemies[target]

            # If Casting
            elif action == 1:
                # Choosing Magic and Initialization
                player.magic_choice()
                magic_spell = int(input("\nChoose Magic:"))-1

                # Exit
                if magic_spell == -1:
                    continue

                spell = player.mg[magic_spell]
                magic_dmg = spell.generate_spell_dmg()
                print("____________________________________")

                if spell.type == "White":
                    if player.get_mp() < spell.cost:
                        print(bcolors.FAIL + "Not Enough Mana" + bcolors.ENDC)
                        print("____________________________________")
                        continue
                    else:
                        # MP Reduction
                        player.reduce_mp(spell.cost)

                        # Heal player
                        target = player.heal_target(players)
                        players[target].heal(magic_dmg)

                        # String Output
                        print(bcolors.OKBLUE + "Cast:", spell.name, bcolors.ENDC)
                        print(bcolors.OKBLUE + "Healed for:", magic_dmg, bcolors.ENDC)
                        print("____________________________________")
                elif spell.type == "Black":
                    if player.get_mp() < spell.cost:
                        print(bcolors.FAIL + "Not Enough Mana" + bcolors.ENDC)
                        print("____________________________________")
                        continue
                    else:
                        # HP Reduction
                        target = player.choose_target(enemies)
                        enemies[target].take_dmg(magic_dmg)

                        # MP Reduction
                        player.reduce_mp(spell.cost)

                        # String Output
                        print(bcolors.OKBLUE + "You Cast " + spell.name + " Remaining MP:",
                              player.get_mp(), bcolors.ENDC)
                        print("\nAttacked", enemies[target].name, "for", magic_dmg)
                        print("____________________________________")

                        # Remove enemy from attacking list
                        if enemies[target].get_hp() == 0:
                            print("\n", enemies[target].name, "is Dead")
                            print("____________________________________")
                            del enemies[target]

            elif action == 2:
                # Choose Item
                player.item_choice()
                choose_item = int(input("\nChoose Item:"))-1
                print("____________________________________")

                # Exit
                if choose_item == -1:
                    continue

                # Get Item and Quantity from Item Dictionary
                item = player.items[choose_item]["item"]

                if player.items[choose_item]["quantity"] == 0:
                    # Check if Item is Zero
                    print(bcolors.FAIL + "\nNo", player.items[choose_item]["item"].name, "Left" + bcolors.ENDC)
                    print("____________________________________")
                    continue

                # Reduce Item
                player.items[choose_item]["quantity"] -= 1

                if item.type == "Potion":
                    # Potion Heal
                    player.heal(item.prop)
                    print(bcolors.OKBLUE + "Used " + item.name, bcolors.ENDC)
                    print("Healed for", item.prop)
                    print("____________________________________")

                elif item.type == "Elixir":
                    if item.name == "High Elixir":
                        for party in players:
                            party.heal(item.prop)
                            party.restore(item.prop)
                            print(bcolors.OKBLUE + "Used " + item.name, bcolors.ENDC)
                            print("Party HP / MP Restored", item.prop)
                            print("____________________________________")
                            print("helixer used")
                    else:
                        player.heal(item.prop)
                        player.restore(item.prop)
                        print(bcolors.OKBLUE + "Used " + item.name, bcolors.ENDC)
                        print("Healed and Restored for", item.prop)
                        print("____________________________________")

                elif item.type == "Attack":
                    # Damage Generation and HP reduction
                    dmg = item.prop
                    target = player.choose_target(enemies)
                    enemies[target].take_dmg(dmg)

                    # String Output
                    print(bcolors.OKGREEN + "Used " + item.name, bcolors.ENDC)
                    print("\nAttacked", enemies[target].name, "for", dmg)
                    print("____________________________________")

                    # Remove enemy from attacking list
                    if enemies[target].get_hp() == 0:
                        print("\n", enemies[target].name, "is Dead")
                        print("____________________________________")
                        del enemies[target]

    for enemy in enemies:
        enemy_action = random.randrange(0, 2)
        target = random.randrange(0, 3)

        # Enemy Health Check
        # Prints success 3 times weird
        if enemy1.get_hp() == 0 and enemy2.get_hp() == 0 and enemy3.get_hp() == 0:
            print(bcolors.OKGREEN + "\nEnemy Dead, You Won!" + bcolors.ENDC)
            print("____________________________________")
            run = False
        else:
            if enemy.get_hp() != 0:
                if enemy_action == 0:
                    # Enemy Attack Generation and Player HP Reduction
                    enemy_dmg = enemy.generate_damage()
                    players[target].take_dmg(enemy_dmg)

                    # String Output
                    print("\n", enemy.name, "attacked", players[target].name, "for", enemy_dmg)
                    print("____________________________________")

                elif enemy_action == 1:
                    spell, magic_dmg = enemy.choose_enemy_magic()
                    enemy.reduce_mp(spell.cost)

                    if spell.type == "White":
                        enemy.heal(magic_dmg)
                        print("\n", enemy.name, "Cast", spell.name, "Healed for", magic_dmg)
                        print("____________________________________")
                    elif spell.type == "Black":
                        players[target].take_dmg(magic_dmg)
                        print("\n", enemy.name, "Cast", spell.name, "Attacked", players[target].name, "for", magic_dmg)
                        print("____________________________________")

                        if players[target].get_hp() == 0:
                            print("\n", players[target].name, "is Dead")
                            print("____________________________________")
                            del players[target]

    # Player Health Check
    if player1.get_hp() == 0 and player2.get_hp() == 0 and player3.get_hp() == 0:
        print(bcolors.FAIL + "You Died, You Lost!" + bcolors.ENDC)
        run = False