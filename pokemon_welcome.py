from os import system, name

from time import sleep

from threading import Event

#import pygame

from img_ascii import *

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
    print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
    print()
    print("**** WELCOME TRAINER!****")
    Event().wait(1)
    print("*** TO ***")
    Event().wait(1)
    clear()
    title_img3()
    print()
    print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
    ekans_img()

    # 5 second delay
    Event().wait(5)
    
    clear()
    
    input("Press ENTER to continue")

    clear()

def intro():
    print("While walking through a forest, you lose track of your friends... \n")
    Event().wait(3)
    print("Luckily, you have your faithful pokemon with you.")

    #placeholder pokemon selection screen


welcome_menu()
intro()
    