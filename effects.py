import time,os,sys
from os import system, name
from time import sleep

def invalid_input():
  print("I do not comprehend. You make my head hurt.")
  time.sleep(3)

def room_enter():
  clear()
  loading()
  clear()

#typing text effect
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

#time display
t = time.localtime()
current_time = time.strftime("%H:%M", t)

#clear screen
def clear():
    #for windows
    if name == "nt":
        _ = system("cls")
    
    #for mac/linux
    else:
        _ = system("clear")

#loading ellipsis
def loading():                                      
    spaces = 0                                      #making a variable to store the amount of spaces between the start and the "."                                     
    timeout = 5                                     # [seconds]
    timeout_start = time.time()

    while time.time() < timeout_start + timeout:    #5 sec loop
        print("\b "*spaces+".", end="", flush=True) #we are deleting however many spaces and making them " " then printing "."
        spaces = spaces+1                           #adding a space after each print
        time.sleep(0.2)                             #waiting 0.2 secconds before proceeding
        if (spaces>5):                              #if there are more than 5 spaces after adding one so meaning 5 spaces (if that makes sense)
            print("\b \b"*spaces, end="")           #delete the line
            spaces = 0                              #set the spaces back to 0

