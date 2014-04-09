import sys
import os
 
 
def create(filename):
     
#cree du fond
    bg=dict()
#ouvrir le fichier texte fond.txt
     
    myfile=open(filename,"r")
     
    chaine=myfile.read()
     
    #separation des lignes
    listeLignes=chaine.splitlines()
    bg["map"]=[]
     
 
#transformation en liste de listes
    for line in listeLignes:
        listeChar=list(line)
        bg["map"].append(listeChar)
    myfile.close()
     
 
    return bg
     
 
 
def getChar(bg,x,y):
 #renvoie contenue d une case donnee
    return (bg["map"][y-1][x-1])
 
def setChar(bg,x,y,c):
    #change le contenu d'une case donnee
    bg["map"][y-1][x-1]=c
 
 
def show(bg):
    #couleur fond
    sys.stdout.write("\033[40m")
    #couleur char
    sys.stdout.write("\033[37m")
     
    #goto
 
    for y in range(0,len(bg["map"])):
        for x in range(0,len(bg["map"][y])):
            s="\033["+str(y+1)+";"+str(x+1)+"H"
            sys.stdout.write(s)
            #affiche
            sys.stdout.write(bg["map"][y][x])
             
#def getSpawn(bg):
 #   for y in range(0,len(bg["map"])):
  #      for x in range(0,len(bg["map"][y])):
   #         if getChar(bg,x,y)=='0':
    #            spawn=tuple(x,y)