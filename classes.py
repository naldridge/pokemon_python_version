class Pokemon:
    def __init__(self, name, health, first_attack, second_attack, third_attack, fourth_attack):
        self.name = name
        self.health = health
        self.first_attack = first_attack
        self.second_attack = second_attack
        self.third_attack = third_attack
        self.fourth_attack = fourth_attack

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_party = []
    def __str__(self):
        return 'Pokemon: %s' % (self.name)
    def add_pokemon(self, pokemon):
        self.pokemon_party.append(pokemon)
    def num_pokemon(self):
        for pokemon in self.pokemon_party:
            print(pokemon.name)

        
class Fire(Trainer):
    def __init__(self, name, health, fire_blast, wing_attack, slash, flamethrower):
        self.name = name
        self.health = health
        self.fire_blast = fire_blast
        self.wing_attack = wing_attack
        self.slash = slash
        self.flamethrower = flamethrower
    def main_attack(self, enemy):
        enemy.health -= self.fire_blast
    def secondary_attack(self, enemy):
        enemy.health -= self.wing_attack

class Water(Trainer):
    def __init__(self, name, health, hydro_pump, crunch, headbutt, surf):
        self.name = name
        self.health = health
        self.hydro_pump = hydro_pump
        self.crunch = crunch
        self.headbutt = headbutt
        self.surf = surf
    def main_attack(self, enemy):
        enemy.health -= self.hydro_pump

class Grass(Trainer):
    def __init__(self, name, health, solarbeam, sludge_bomb, secret_power, giga_drain):
        self.name = name
        self.health = health
        self.solarbeam = solarbeam
        self.sludge_bomb = sludge_bomb
        self.secret_power = secret_power
        self.giga_drain = giga_drain
    def main_attack(self, enemy):
        enemy.health -= self.solarbeam

houndoom = Fire("Houndoom", 110, 50, 30, 30, 40)
charizard = Fire("Charizard", 110, 50, 30, 30, 40)
blastoise = Water("Blastoise", 130, 40, 25, 25, 30)
venusaur = Grass("Venusaur", 150, 40, 25, 25, 25)
trainer = Trainer("Rodrigo")

running = True

while running:
    print("1. Charizard")
    print("2. Venusaur")
    print("3. Check party")
    print("4. Finished")
    add_pokemon = input("Add the pokemon to your list ")
    if add_pokemon == "1":
        trainer.add_pokemon(charizard)
    elif add_pokemon == "2":
        trainer.add_pokemon(venusaur)
    elif add_pokemon == "3":
        trainer.num_pokemon()
    elif add_pokemon == "4":
        running = False

        


# Beginning of battle prompt
while True:
    print("Sean wants to fight!")
    print("Sean sent out Blastoise!")
    print("")
    print("1. Charizard")
    print("2. Venusaur")
    print("3. Run")
    pokemon_choice = input("What pokemon would you like to use? ")
    if pokemon_choice == "1":
        # User chose Charizard
        print("")
        print("Go Charizard!")
        print("")
        while charizard.health > 0 and blastoise.health > 0:
            print("What would you like to do? ")
            print("1. Fire Blast")
            print("2. Wing Attack")
            print("3. Slash")
            print("4. Flamethrower")
            user_input = input()
            if user_input == "1":
                #User chose Fire Blast
                charizard.main_attack(blastoise)
                print("You use %s on %s. Blastoise now has %d health" % ("Fire Blast", blastoise.name, blastoise.health))
                if blastoise.health > 0:
                    blastoise.main_attack(charizard)
                    print("%s used %s. %s now has %d health." % (blastoise.name, "Hydro Pump", charizard.name, charizard.health))
                    if charizard.health <= 0:
                        print("Charizard has fainted, you lose the battle")
                else:
                    print("Blastoise has fainted, you won the battle!")
            if user_input == "2":
                # User chose Wing Attack
                charizard.secondary_attack(blastoise)
                print("You use %s on %s. Blastoise now has %d health" % ("Wing Attack", blastoise.name, blastoise.health))
                if blastoise.health > 0:
                    blastoise.main_attack(charizard)
                    print("%s used %s. %s now has %d health." % (blastoise.name, "Hydro Pump", charizard.name, charizard.health))
                    if charizard.health <= 0:
                        print("Charizard has fainted, you lose the battle")
                else:
                    print("Blastoise has fainted, you won the battle!")
            if user_input == "3":
                quit()
    elif pokemon_choice == "2":
        # User chose Venusaur
        print("")
        print("Go Venusaur!")
        print("")        
        while venusaur.health > 0 and blastoise.health > 0:
            print("What would you like to do? ")
            print("1. Solarbeam")
            print("2. Sludge Bomb")
            print("3. Secret Power")
            print("4. Giga Drain")
            user_input = input()
            if user_input == "1":
                # User chose Solarbeam
                venusaur.main_attack(blastoise)
                print("You use %s on %s. Blastoise now has %d health" % ("Solarbeam", blastoise.name, blastoise.health))
                if blastoise.health > 0:
                    blastoise.main_attack(venusaur)
                    print("%s used %s. %s now has %d health." % (blastoise.name, "Hydro Pump", venusaur.name, venusaur.health))
                    if venusaur.health <= 0:
                        print("Venusaur has fainted, you lose the battle")
                else:
                    print("Blastoise has fainted. Trainer is out of pokemon, you won the battle!")
            if user_input == "2":
                # User chose Sludge Bomb
                venusaur.secondary_attack(blastoise)
                print("You use %s on %s. Blastoise now has %d health" % ("Sludge Bomb", blastoise.name, blastoise.health))
                if blastoise.health > 0:
                    blastoise.main_attack(venusaur)
                    print("%s used %s. %s now has %d health." % (blastoise.name, "Hydro Pump", venusaur.name, venusaur.health))
                    if venusaur.health <= 0:
                        print("Venusaur has fainted, you lose the battle")
                else:
                    print("Blastoise has fainted. Trainer is out of pokemon, you won the battle!")
            if user_input == "3":
                quit()
    if pokemon_choice == "3":
        print("You avoided the battle")
        quit()
