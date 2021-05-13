from os import system, name

from time import sleep

import pygame
#pygame.init()


def clear():
    #for windows
    if name == "nt":
        _ = system("cls")
    
    #for mac/linux
    else:
        _ = system("clear")


def welcome_menu():
    clear()
    print("><><><><><><><><><><><><><><><><><><><><><><><")
    print()
    print("**** WELCOME TRAINER! TO POKEMON ****")
    print()
    print("><><><><><><><><><><><><><><><><><><><><><<><")
    start_prompt = input("Are you ready to get started? y or n \n")
    if start_prompt == "y":
        clear()
        print("Excellent! Let us begin...")
    elif start_prompt == "n":
        print("We will be here when you're ready.")
        exit
    else:
        print("I think you may be confused. Come back when you are ready to begin.")
        exit

def intro():
    print("While walking through a forest, you lose track of your friends... \n")
    print("Luckily, you have your faithful pokemon with you.")

    #placeholder pokemon selection screen


welcome_menu()
intro()
    