from classes.game import Person, bcolors


magic = [{"name": "Fire", "Cost": 10, "dmg": 60},
         {"name": "Thunder", "Cost": 10, "dmg": 80},
         {"name": "Blizzard", "Cost": 10, "dmg": 60}]


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
        print("Bravo , Your impact in Enemy is ", dmg, "points , Now Enemy HP :", enemy.get_hp())

    enemy_choice = 1 

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy Inflicted ", enemy_dmg, "Points Damage Now Your  HP : ", player.get_hp())