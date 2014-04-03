#modules externes
import sys
import os
import time
import select
import tty 
import termios
#nos modules
import background
import monster
#donnees du jeu
myBackground=None
myMonster=None
timeStep=None




def init():
	global myBackground,myMonster, timeStep



	#initialisation de la partie
	timeStep=0.2

	#creation des elements du jeu
	myMonster=monster.create(color=4,
		direction="right",
		x=5.0,
		y=5.0,
		xMax=40.0,
		yMax=40.0,
		speed=3.0
		)

	myBackground=background.create("background.txt")



def show():
	global background

	#effacer la console
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")

	#affichage des different element
	background.show(myBackground)
	

	#restoration couleur 
	sys.stdout.write("\033[39m")
	sys.stdout.write("\033[61m")

	#deplacement curseur
	sys.stdout.write("\033[0;0H\n")

def run():
	global timeStep

	#boucle de simulation
	while 1:
		show()
		time.sleep(timeStep)

init()

