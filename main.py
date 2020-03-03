from classes.game import Person, bcolors


magic = [{"name": "Fire", "cost": 15, "dmg": 152},
         {"name": "Thunder", "cost": 10, "dmg": 137},
         {"name": "Blizzard", "cost": 8, "dmg": 105}]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)


#print(player.generate_spell_damage(0))
#print(player.generate_spell_damage(1))

running = True 
i = 0

print(bcolors.FAIL + bcolors.BOLD + "THE ENEMY IS APPROACHING! AND CAN ATTACK ANYTIME SOON !" + bcolors.ENDC)


while running:
    print("===================================")
    player.chose_action()
    choice = input ("Choose action:")
    index = int(choice) -1
   #print("You chose", player.get_spell_name(int(index)))

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("Bravo , Your impact in Enemy is ", dmg, " points")

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) -1 
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nYou Dont Have Enough Magic Powers\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "Points of damage" + bcolors.ENDC)

    enemy_choice = 1 

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy Inflicted ", enemy_dmg, "Points Damage")

    print("-------------------------------------------")

    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)

    print("Your MP :", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC +  "\n")


    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN  + "You are the DISTROYER!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You Are DiSTROYED" + bcolors.ENDC)
        running = False

