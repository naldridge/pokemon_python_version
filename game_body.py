from os import system, name
from time import sleep
import time,os,sys
from effects import *
from img_ascii import *
from battle import *
from validate import *
from trainer_class import *
from trainer_class import Trainer
from trainer_class import Enemy
from pokemon_class import Pokemon
from pokemon_class import Attack
from trainer_class import Trainer
from trainer_class import Enemy
from pokemon_class import Pokemon
from pokemon_class import Attack
from pokemon_welcome import welcome_menu

welcome_menu()



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
grimer_attacks = [acid, feint_attack, tackle, scratch]
raticate_attacks = [slash, feint_attack, tackle, scratch]

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
grimer = Pokemon("Grimer", 110, 110, grimer_attacks)
raticate = Pokemon("Raticate", 120, 120, raticate_attacks)

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
chris = Enemy("Chris", [grimer, raticate])
trainer = Trainer(trainer_name, pokemon_party)

def choose_pokemon(trainer, choices):
    count = 0
    while len(choices) > count:
        print(f'{count + 1}. {choices[count].name}')
        count += 1
    user_input = Validate().range(1, len(choices), "please enter a valid option. ", " select a pokemon you would like to add to your party.")
    trainer.pokemon_party.append(choices[user_input - 1])
    print(f'You chose {choices[user_input - 1].name}!')
    time.sleep(1)
    choices.remove(choices[user_input - 1])
    clear()

def intro():
    print("While walking through a forest, you lose track of your friends... \n")
    time.sleep(3)
    print("Luckily, you have your faithful pokemon with you.")
    time.sleep(3)
    clear()
    oak_img()
    time.sleep(2)
    choose_pokemon(trainer,options)
    one_img()
    choose_pokemon(trainer,options)
    two_img()
    choose_pokemon(trainer,options)
    three_img()
    trainer.num_pokemon()
    time.sleep(3)


def game_start():
    #while self.trainer.pokemon_party > 0():
    print("Oh that's right! Those are your pokemon.")
    time.sleep(2)
    print("Ahead you see a cave entrance. What would you like to do?")
    time.sleep(1)
    print("1. Investigate!")
    print("2. Check your watch?")
    print("3. Run Away!!")
    print(">",)
    user_input = input()
    if user_input == "1":
        print("It appears to be a secret hideout!")
        time.sleep(3)
        print("Let's check it out!")
        time.sleep(3)
        #Proceed to Gym Entrance
        gym_entrance()
    elif user_input =="2":
        print("Your watch shows it is " + current_time)
        time.sleep(1.5)
        print("Would you like to check out that cave entrance now? y or n")
        user_input = input()
        if user_input == "y":
            print("It appears to be a secret hideout!")
            time.sleep(3)
            print("Let's check it out!")
            time.sleep(3)
            #Proceed to Gym Entrance
            gym_entrance()
        else:
            print("Your friends return and take you back to your village.")
            print("Thanks for playing!")
            exit()
    elif user_input =="3":
        print("That's probably smart. Nothing good comes from being nosey.")
        time.sleep(4)
        print("Thanks for playing.")
        exit()
    else:
        invalid_input()

def gym_entrance():
    room_enter()
    print("Who could be hiding out here?")
    time.sleep(3)
    print("As you approach the cave you see a door.")
    while True:
        print("1. Open door?")
        print("2. Turn back now.")
        print(">",)
        user_input = input()
        if user_input == "1":
            #battle time!
            print("You hear someone coming!")
            time.sleep(3)
            clear()
            typingPrint("\"Trying to sneak up on Team Rocket, are ya?\"\n")
            time.sleep(1)
            typingPrint("\"We'll see about that.\"")
            time.sleep(2)
            battle_sam.battle()
            hideout_enter()
        elif user_input == "2":
            #battle time anyways
            print("It's too late now!")
            time.sleep(3)
            clear()
            typingPrint("\"Trying to sneak up on Team Rocket, are ya?\"\n")
            time.sleep(1)
            typingPrint("\"We'll see about that.\"")
            time.sleep(2)
            battle_sam.battle()
            hideout_enter()
        else:
            invalid_input()
       

def battle1():
    clear()
    typingPrint("\"Trying to sneak up on Team Rocket, are ya?\"\n")
    time.sleep(1)
    typingPrint("\"We'll see about that.\"")
    time.sleep(2)
    #run battle
    
    battle_sam.battle()
    hideout_enter()

def hideout_enter():
    clear()
    print("Great work, Trainer! Something tells me the rest of Team Rocket won't be so easy.")
    time.sleep(3)
    room_enter()
    print("You enter Team Rocket's Hideout only to find it bustling with people training their pokemon.")
    time.sleep(3)
    print("This will definitely be harder than you thought.")
    time.sleep(3)
    print("Luckily everyone seems to be too busy to notice you barging in.")
    time.sleep(3)
    print("As you look around you see so many pokemon.")
    time.sleep(3)
    print("After wandering around the room you find yourself in a hallway.")
    time.sleep(3)
    clear()
    hallway1_initial()

def hallway1_initial():
    print("The hallway looks to be empty.")
    time.sleep(3)
    print("Posters adorn the walls.")
    time.sleep(3)
    print("You get an ominous feeling.")
    time.sleep(3)
    print("As you move deeper into the hallway, you hear music coming from the speakers.")
    #cue sci-fi music, disney or sci-fi
    time.sleep(3)
    while True:
        print("What would you like to do?")
        print("1. Look for a door?")
        print("2. Examine a nearby poster?")
        print("3. Listen to the music for a bit?")
        print("4. Keep moving.... This is creepy.")
        print(">",)
        user_input = input()
        if user_input == "1":
            print("What do you know! There is a door on your right. Go check it out.")
            #Enter hideout store
            general_store()
        elif user_input == "2":
            print("Is that a movie poster from Tron? What an odd reference in a place like this.")
            time.sleep(5)
            clear()
        elif user_input == "3":
            print("Yeah. Just take a break. Everyone needs a little self-care once in awhile.")
            #music volume increases for 9 secs?
            time.sleep(10)
            clear()
        elif user_input == "4":
            print("Smart... It's not like there is a general store behind that door or anything.")
            hallway2()
        else:
            invalid_input()

def hallway1_revisit():
    room_enter
    print("The hallway still looks to be empty.")
    time.sleep(3)
    print("Posters adorn the walls.")
    time.sleep(3)
    print("You get an ominous feeling.")
    time.sleep(3)
    print("As you move deeper into the hallway, you hear music coming from the speakers.")
    #cue sci-fi music, disney or sci-fi
    time.sleep(3)
    while True:
        print("What would you like to do?")
        print("1. Look for a door?")
        print("2. Examine a nearby poster?")
        print("3. Listen to the music for a bit?")
        print("4. Keep moving.... This is creepy.")
        print(">",)
        user_input = input()
        if user_input == "1":
            print("What do you know! There is a door on your right. Go check it out.")
            #Enter hideout store
            #general_store()
        elif user_input == "2":
            print("Is that a movie poster from Tron? What an odd reference in a place like this.")
            time.sleep(5)
            clear()
        elif user_input == "3":
            print("Yeah. Just take a break. Everyone needs a little self-care once in awhile.")
            #music volume increases for 9 secs?
            time.sleep(10)
            clear()
        elif user_input == "4":
            print("Smart... It's not like there is a general store behind that door or anything.")
            hallway3_revisit()
        else:
            invalid_input()

def hallway2():
    #start with another battle
    clear()
    print("You see that the hallway turns a corner not far away.")
    time.sleep(3)
    print("However before you can take 2 steps, someone jumps out from behind a giant DeathStar replica.")
    time.sleep(3)
    typingPrint("\"Hey who let you in here?!\"\n")
    time.sleep(3)
    typingPrint("\"Well it doesn't matter. Let me show you a cool way to leave... By taking a beating.\"\n")
    time.sleep(3)
    #run battle2
    battle_chris.battle()
    hallway3_initial()

def hallway3_initial():
    room_enter()
    print("That was much harder than the last battle.")
    time.sleep(3)
    print("How about you see what's around that corner now?")
    time.sleep(4)
    hallway3_main()

def hallway3_main():
    room_enter()
    print("As you round the corner you're startled by a statue of Mickey Mouse.")
    time.sleep(3)
    print("Someone really likes Disney here.")
    time.sleep(3)
    print("Once you recover from your shock, you examine the hallway more closely.")
    time.sleep(3)
    print("You see a door to your left, a door to your right and only a few steps down is another door at the end of the hall.")
    time.sleep(3)
    while True:
        print("What would you like to do?")
        print("1. Check the door to the right?")
        print("2. Check the door to the left?")
        print("3. Move to the door at the end?")
        print("4. Turn back.")
        print(">",)
        user_input = input()
        if user_input == "1":
            print("This door looks shabby and rundown.")
            time.sleep(3)
            print("Let's see what's inside.")
            time.sleep(3)
            #enter treasure room
            treasure_room()
        elif user_input == "2":
            print("This door looks fancy.")
            time.sleep(3)
            print("What do you think could be inside?")
            time.sleep(3)
            print("Let's go in!")
            time.sleep(3)
            #enter trainer room
            trainer_room()
        elif user_input == "3":
            print("Really? Skip the other rooms? I guess you know best.")
            time.sleep(3)
            #proceed to final boss
            final_boss_room()
        elif user_input == "4":
            print("I think you might have missed something back there... Go check it out.")
            time.sleep(3)
            hallway1_revisit()
        else:
            invalid_input()

def hallway3_revisit():
    room_enter()
    print("As you round the corner that freaking mouse startles you again.")
    time.sleep(3)
    print("Once you recover from your shock, you examine the hallway more closely.")
    time.sleep(3)
    print("You see a door to your left, a door to your right and only a few steps down is another door at the end of the hall.")
    time.sleep(3)
    while True:
        print("What would you like to do?")
        print("1. Check the door to the right?")
        print("2. Check the door to the left?")
        print("3. Move to the door at the end?")
        print("4. Turn back.")
        print(">",)
        user_input = input()
        if user_input == "1":
            print("This door looks shabby and rundown.")
            time.sleep(3)
            print("Let's see what's inside.")
            time.sleep(3)
            #enter treasure room
            treasure_room()
        elif user_input == "2":
            print("This door looks fancy.")
            time.sleep(3)
            print("What do you think could be inside?")
            time.sleep(3)
            print("Let's go in!")
            time.sleep(3)
            #enter trainer room
            trainer_room()
        elif user_input == "3":
            print("Really? Skip the other rooms? I guess you know best.")
            time.sleep(3)
            #proceed to final boss
            final_boss_room()
        elif user_input == "4":
            print("I think you might have missed something back there... Go check it out.")
            time.sleep(3)
            hallway1_revisit()
        else:
            invalid_input()

def treasure_room():
    room_enter()
    print("What is this!?")
    time.sleep(3)
    print("You seem to have entered into a treasure room.")
    time.sleep(3)
    print("There are countless gold statues of cats for some reason...")
    time.sleep(3)
    print("Tapestries of legendary pokemon adorn the walls.")
    time.sleep(3)
    print("In the back there seems to be an open chest.")
    time.sleep(3)
    print("That was pretty careless. Check out the chest?")
    while True:
        print("y or n")
        print(">",)
        user_input = input()
        if user_input == "y":
            print("You see a bag of coins sitting at the top.")
            time.sleep(3)
            print("You grab it.")
            time.sleep(3)
            print("This would be handy if you had found a place to buy items...")
            time.sleep(3)
            break
        elif user_input == "n":
            print("Morals. It's a bold strategy, Cotton. Let's see if it pays off for him.")
            time.sleep(3)
            break
        else:
            invalid_input()
    print("There doesn't seem to be anything else.")
    time.sleep(3)
    print("You decide to head back to the hallway.")
    time.sleep(3)
    hallway3_revisit()

def trainer_room():
    room_enter()
    print("This room looks similar to the large training room when you first walked in.")
    time.sleep(3)
    print("However, you notice right away the trainers in here are much more skilled.")
    time.sleep(3)
    print("Before you can turn around you see someone from the back stalking straight towards you.")
    time.sleep(3)
    typingPrint("\"You must be pretty skilled to have made it this far into the Team Rocket Hideout.\"\n")
    time.sleep(3)
    typingPrint("\"I'm excited to see what you're capable of. Maybe I can give you some tips.\"\n")
    time.sleep(3)
    battle_zachary.battle()
    hallway3_revisit()

def final_boss_room():
    room_enter
    print("Looks like you made it.")
    time.sleep(3)
    print("Before you stands a solid door. No embellishments.")
    time.sleep(3)
    print("There can be no denying who stands behind this door.")
    time.sleep(3)
    print("Now would be a good time to use any items in your inventory...")
    time.sleep(3)
    #pause for an inventory check
    print("Are you ready?")
    time.sleep(2)
    print("LLLLEEEERRRROOOOYYY JJJJJJJJEEEENNNNNKKKIIIINNNSSSS!!!!!")
    time.sleep(5)
    clear()
    print("You burst through the door and the first thing you notice is the music.")
    time.sleep(3)
    #cue boss music
    print("Boss music.")
    time.sleep(3)
    print("A bearded man stands before you. Waiting.")
    time.sleep(3)
    typingPrint("\"Look what we heva here.\"\n")
    time.sleep(3)
    typingPrint("\"Ugh stupid spelling.\"\n")
    time.sleep(3)
    typingPrint("\"Always check your spelling.\"\n")
    time.sleep(3)
    typingPrint("\"Well no time like the present. You must be strong.\"\n")
    time.sleep(3)
    battle_sean.battle()


battle_sam = Battle(trainer,sampai)
battle_zachary = Battle(trainer,zachary)
battle_chris = Battle(trainer,chris)
battle_sean = Battle(trainer,sean)



intro()
game_start()