from trainer_class import Trainer
from trainer_class import Enemy
from pokemon_class import Pokemon
from pokemon_class import Attack





flamethrower = Attack("Flamethrower", 40)
fire_blast = Attack("Fire Blast", 50)
waterfall = Attack("Waterfall", 40)
hydro_pump = Attack("Hydro Pump", 50)
giga_drain = Attack("Giga Drain", 40)
solar_beam = Attack("Solar Beam", 50)
wing_attack = Attack("Wing Attack", 35)
drill_peck = Attack("Drill Peck", 40)
fly = Attack("Fly", 50)
tackle = Attack("Tackle", 30)
scratch = Attack("Scratch", 35)
rapid_spin = Attack("Rapid Spin", 35)
slash = Attack("Slash", 35)
mega_punch = Attack("Mega Punch", 35)
tri_attack = Attack("Tri Attack", 40)
hyperbeam = Attack("Hyperbeam", 55)
feint_attack = Attack("Feint Attack", 35)
pay_back = Attack("Pay Back", 40)
crunch = Attack("Crunch", 40)
thunder_bolt = Attack("Thunder Bolt", 35)
thunder = Attack("Thunder", 50)
high_jump_kick = Attack("High Jump Kick", 50)
confusion = Attack("Confusion", 40)
psychic = Attack("Psychic", 60)
psybeam = Attack("Psybeam", 50)
sludge_bomb = Attack("Sludge Bomb", 40)
acid = Attack("Acid", 40)
ice_punch = Attack("Ice Punch", 35)
ice_beam = Attack("Ice Beam", 50)
play_rough = Attack("Play Rough", 40)


#
persian_attacks = [scratch, play_rough, feint_attack, pay_back]
mewtwo_attacks = [psychic, confusion, tri_attack, ice_beam]
koffing_attacks = [sludge_bomb, pay_back, acid, tackle]
houndoom_attacks = [fire_blast, crunch, feint_attack, flamethrower]
murkrow_attacks = [wing_attack, drill_peck, tackle, pay_back]
arbok_attacks = [sludge_bomb, crunch, acid, feint_attack]

# Pokemon attack list
charizard_attacks = [flamethrower, wing_attack, slash, fire_blast]
blastoise_attacks = [hydro_pump, waterfall, rapid_spin, crunch]
venusaur_attacks = [solar_beam, sludge_bomb, acid, giga_drain]
alakazam_attacks = [confusion, psybeam, tri_attack, flamethrower]
snorlax_attacks = [hyperbeam, mega_punch, ice_punch, crunch]
gyarados_attacks = [hydro_pump, waterfall, drill_peck, crunch]
machamp_attacks = [high_jump_kick, mega_punch, pay_back, ice_punch]
electabuzz_attacks = [thunder, thunder_bolt, slash, play_rough]
pidgeot_attacks = [wing_attack, drill_peck, slash, fly]

# Enemy Pokemon
persian = Pokemon("Persian", 130, 130, persian_attacks)
mewtwo = Pokemon("Mewtwo", 150, 140, mewtwo_attacks)
koffing = Pokemon("Koffing", 120, 120, koffing_attacks)
houndoom = Pokemon("Houndoom", 130, 130, houndoom_attacks)
murkrow = Pokemon("Murkrow", 120, 120, murkrow_attacks)
arbok = Pokemon("Arbok", 130, 130, arbok_attacks)

# User Pokemon
charizard = Pokemon("Charizard", 110, 110, charizard_attacks)
blastoise = Pokemon("Blastoise", 125, 125, blastoise_attacks)
venusaur = Pokemon("Venusaur", 125, 125, venusaur_attacks)
alakazam = Pokemon("Alakazam", 110, 110, alakazam_attacks)
snorlax = Pokemon("Snorlax", 170, 170, snorlax_attacks)
gyarados = Pokemon("Gyarados", 120, 120, gyarados_attacks)
machamp = Pokemon("Machamp", 120, 120, machamp_attacks)
electabuzz = Pokemon("Electabuzz", 120, 120, electabuzz_attacks)
pidgeot = Pokemon("Pidgeot", 120, 120, pidgeot_attacks)


pokemon_party = []
options = [charizard, blastoise, venusaur, alakazam, snorlax, gyarados, machamp, electabuzz, pidgeot]

trainer_name = input("Enter a name ")
sean = Enemy("Team Rocket Leader Sean", [persian, mewtwo])
sampai = Enemy("Sam-pai", [murkrow, arbok])
zachary = Enemy("Zachary", [koffing, houndoom])
trainer = Trainer(trainer_name, pokemon_party)