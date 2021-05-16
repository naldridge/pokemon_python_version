import time,os,sys
from os import system, name
from time import sleep


def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def current_time():
  t = time.localtime()
  current_time = time.strftime("%H:%M", t)

  

def clear():
    #for windows
    if name == "nt":
        _ = system("cls")
    
    #for mac/linux
    else:
        _ = system("clear")