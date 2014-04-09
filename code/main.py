#modules externes
import sys
import os
import time
import select
import tty
import termios
 
#mes modules
import map
 
#donnee du jeu
myBackground=None
timeStep=None
 
 
 
def main():
    pass
     
 
 
 
def init():
    global myBackground, timeStep
 
    #initialisation de la partie
    timeStep=0.2
    #creation des elements du jeu
    myBackground=map.create("fond.txt")
 
 
def run():
    global timeStep
     
    #boucle de simulation
    while 1:
        show()
        time.sleep(timeStep)
 
        #effacement de la console
        sys.stdout.write("\033[1;1H")
        sys.stdout.write("\033[2J")
 
 
 
 
def show():
    global myBackground
    #affiche des differents ellements du jeu
    map.show(myBackground)
   # print map.getSpawn(myBackground)
    #restoration couleur
     
    #deplacement curseur
    sys.stdout.write("\033[1;1H\n")
 
def interact():
    pass
 
def move():
    pass
 
 
def askName():
    pass
     
 
 
def askLevel():
    pass
     
 
 
 
 
init()
run()