import sys
import os

def create(filename):
	#creation du fond
	bg=dict()

	#ouvre fichier .txt

	myfile=open(filename,"r")
	bg["str"]=myfile.read()
	myfile.close()

	return bg

def show(bg):
	#goto
	sys.stdout.write("\033[1;1H")
	
	#couleur fond 
	sys.stdout.write("\033[46m")

	
	#affiche
	sys.stdout.write(bg["str"])
