#File made by: Kauan, Rafael, Davi.

import random
import os
import time
from assets.config import Char


#Just clear the screen, based on your OS.
def clearScreen():
  if os.name == 'nt':  # Windows
    os.system('cls')
  else:  # Linux ou macOS
    os.system('clear')

#Makes the print like an 'typing' print. You can change the speed by going on 'assets/config.py at the config class'
def typedPrint(text, speed):
  for i in text:
    print(i, end='', flush=True)
    time.sleep(speed)

def classUpdate():
  if Char.Name == "Aton":
    Char.classplayer = 1
    Char.health = 100
    Char.mana = 50
    Char.attack = 1.5
    weaponsInventory.append("Espada gasta")
  else:
    Char.classplayer = 2
    Char.health = 120
    Char.mana = 100
    Char.attack = 1.3
    weaponsInventory.append("Cajado antigo")
