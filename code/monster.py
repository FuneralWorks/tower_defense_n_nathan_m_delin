import sys
import os

def create(color,direction,x,y,xMax,yMax,speed):

	#creation d un monstre
	monster=dict
	monster["color"]=color
	monster["direction"]=direction
	monster["x"]=x
	monster["y"]=y
	monster["xMax"]=xMax
	monster["yMax"]=yMax
	monster["speed"]=speed

	return monster

def show(a):

	#placer monstre a l entree de la map
	x=str(int(a["x"]))
	y=str(int(a["y"]))
	txt="\033["+y+";"+x+"M"
	sys.stdout.write(txt)

	#couleur monstre
	c=a["color"]
	txt="\033[3"+str(c%7+1)+"m"
	sys.stdout.write(txt)

	#affichage du mosntre : le caractere affiche est un coeur
	cara = u"\U0001F47E"
	sys.stdout.write(cara)