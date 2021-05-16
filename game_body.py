from os import system, name
from time import sleep
import time,os,sys
from effects import *
from threading import Event
from img_ascii import *




def intro():
    print("While walking through a forest, you lose track of your friends... \n")
    Event().wait(3)
    print("Luckily, you have your faithful pokemon with you.")

#placeholder pokemon selection screen

def game_start():
    #while self.trainer.pokemon_party > 0():
    print("Oh that's right! Those are your pokemon.")
    Event().wait(2)
    print("Ahead you see a cave entrance. What would you like to do?")
    Event().wait(1)
    print("1. Investigate!")
    print("2. Check your watch?")
    print("3. Run Away!!")
    print(">",)
    user_input = input()
    if user_input == "1":
        print("It appears to be a secret hideout!")
        #Proceed to Gym Entrance
        #break
    elif user_input =="2":
        print("Your watch shows it is " + current_time)
        Event().wait(1.5)
        print("Would you like to check out that cave entrance now? y or n")
        user_input = input()
        if user_input == "y":
            print("It appears to be a secret hideout!")
            #Proceed to Gym Entrance
            #break
        else:
            print("Your friends return and take you back to your village.")
            print("Thanks for playing!")
            exit()
    elif user_input =="3":
        print("That's probably smart. Nothing good comes from being nosey.")
        Event().wait(1)
        print("Thanks for playing.")
        exit()
    else:
        print("Invalid input.")

    print("Let's check it out!")
    clear()
    print("Who could be hiding out here?")
    Event().wait(1)
    print("As you approach the cave you see a door.")
    print("1. Open door?")
    print("2. Turn back now.")
    print(">",)
    user_input = input()
    if user_input == "1":
        #battle time!
        print("You hear someone coming!")
    elif user_input == "2":
        #battle time anyways
        print("It's too late now!")
    else:
        print("I didn't recognize that. 1 or 2")
        user_input = input()
        if user_input == "1":
            #battle time!
            print("you hear someone coming!")
        elif user_input == "2":
            #battle time anyways
            print("It's too late now!")

def battle1():
    clear()
    typingPrint("\"Trying to sneak up on Team Rocket, are ya?\"\n")
    Event().wait(1)
    typingPrint("\"We'll see about that.\"")
    Event().wait(2)
    #run battle

def hideout_enter():
    clear()
    print("Great work, Trainer! Something tells me the rest of Team Rocket won't be so easy.")
    Event().wait(3)
    print("You enter Team Rocket's Hideout only to find it bustling with people training their pokemon.")
    Event().wait(3)
    print("This will definitely be harder than you thought.")
    Event().wait(3)
    print("Luckily everyone seems to be too busy to notice you barging in.")
    Event().wait(3)
    print("As you look around you see so many pokemon.")
    Event().wait(3)
    print("After wandering around the room you find yourself in a hallway.")
    Event().wait(3)




intro()
game_start()
battle1()
hideout_enter()