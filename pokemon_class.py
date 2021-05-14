from trainer_class import Trainer
from trainer_class import Enemy
from battle import Battle

class Pokemon:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
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


houndoom = Pokemon("Houndoom", 110, houndoom_attacks )
electabuzz = Pokemon("Electabuzz", 110, electabuzz_attacks)
snorlax = Pokemon("Snorlax", 200, snorlax_attacks)
charizard = Pokemon("Charizard", 110, charizard_attacks)

sampai = Enemy("Sam-pai", [houndoom, snorlax])
trainer = Trainer("Rodrigo", [electabuzz, charizard])


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

battle_sam = Battle(trainer, sampai)
battle_sam.battle()
