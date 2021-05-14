from trainer_class import Trainer
from trainer_class import Enemy
from battle import Battle
from validate import Validate

class Pokemon:
    def __init__(self, name, health, max_health, attacks):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attacks = attacks

class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

# # Creating Pokemon Attacks
fire_blast = Attack("Fire Blast", 50)
wing_attack = Attack("Wing Attack", 30)
slash = Attack("Slash", 30)
flamethrower = Attack("Flamethrower", 40)
crunch = Attack("Crunch", 35)
feint_attack = Attack("Feint Attack", 30)
thunder = Attack("Thunder", 50)
thunder_bolt = Attack("Thunder Bolt", 35)

houndoom_attacks = [fire_blast, crunch, feint_attack, flamethrower]
electabuzz_attacks = [thunder, thunder_bolt, slash, wing_attack]
snorlax_attacks = [feint_attack, slash, flamethrower, thunder]
charizard_attacks = [flamethrower, wing_attack, slash, fire_blast]
nidoking_attacks = [flamethrower, wing_attack, slash, fire_blast]


houndoom = Pokemon("Houndoom", 110, 110, houndoom_attacks)
electabuzz = Pokemon("Electabuzz", 110, 110, electabuzz_attacks)
snorlax = Pokemon("Snorlax", 200, 200, snorlax_attacks)
charizard = Pokemon("Charizard", 110, 110, charizard_attacks)
nidoking = Pokemon("Nidoking", 120, 120, nidoking_attacks)

pokemon_party = []

sampai = Enemy("Sam-pai", [houndoom, snorlax])
sean = Enemy("Team Rocket Leader Sean", [nidoking, snorlax])
trainer = Trainer("Rodrigo", pokemon_party)



print("""
______     _                               ______      _   _                   _   _               _             
| ___ \   | |                              | ___ \    | | | |                 | | | |             (_)            
| |_/ /__ | | _____ _ __ ___   ___  _ __   | |_/ /   _| |_| |__   ___  _ __   | | | | ___ _ __ ___ _  ___  _ __  
|  __/ _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \  |  __/ | | | __| '_ \ / _ \| '_ \  | | | |/ _ \ '__/ __| |/ _ \| '_ \ 
| | | (_) |   <  __/ | | | | | (_) | | | | | |  | |_| | |_| | | | (_) | | | | \ \_/ /  __/ |  \__ \ | (_) | | | |
\_|  \___/|_|\_\___|_| |_| |_|\___/|_| |_| \_|   \__, |\__|_| |_|\___/|_| |_|  \___/ \___|_|  |___/_|\___/|_| |_|
                                                  __/ |                                                          
                                                 |___/                                                           
""")
input("Press enter to continue")
print("\033c")

running = True
while running:
    print("1. Electabuzz")
    print("2. Charizard")
    print("3. Continue")
    pokemon_choice = input("What pokemon would you like to add to your party? ")
    if pokemon_choice == "1":
        trainer.add_pokemon(electabuzz)
        print("\033c")
        print("You added Electabuzz to your party")
        input("Press enter to continue")
    elif pokemon_choice == "2":
        trainer.add_pokemon(charizard)
        print("\033c")
        print("You added Charizard to your party")
        input("Press enter to continue")
    elif pokemon_choice == "3":
        print("\033c")
        running = False




battle_sam = Battle(trainer, sampai)
battle_sam.battle()

battle_sean = Battle(trainer, sean)
battle_sean.battle()


