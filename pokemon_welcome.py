from os import system, name
from time import sleep
import time,os,sys
from effects import *
from threading import Event
from img_ascii import *




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
    Event().wait(2)
    input("Press ENTER to continue")
    clear()












welcome_menu()

