from os import system, name
from time import sleep
import time
import sys
from threading import Event
#import pygame
from img_ascii import *

#pygame.init()

#random declarations
t = time.localtime()
current_time = time.strftime("%H:%M", t)

def clear():
    #for windows
    if name == "nt":
        _ = system("cls")
    
    #for mac/linux
    else:
        _ = system("clear")


def welcome_menu():
    clear()
    print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
    print("**** WELCOME TRAINER!****")
    Event().wait(1)
    print("*** TO ***")
    Event().wait(1)
    title_img3()
    print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
    Event().wait(3)
    clear()
    ekans_img()

    # 5 second delay
    Event().wait(1)
    
    input("Press ENTER to continue")

    clear()

def intro():
    print("While walking through a forest, you lose track of your friends... \n")
    Event().wait(3)
    print("Luckily, you have your faithful pokemon with you.")

    #placeholder pokemon selection screen

def game_start():
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
            #Proceed to Gym Entrance
        print("It appears to be a secret hideout!")
    elif user_input =="2":
        print("Your watch shows it is " + current_time)
        Event().wait(1.5)
        print("Would you like to check out that cave entrance now? y or n")
        user_input = input()
        if user_input == "y":
            print("It appears to be a secret hideout!")
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

#welcome_menu()
#intro()
    