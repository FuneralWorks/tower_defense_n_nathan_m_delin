

def create(filename):
    # creation du fond
    bg = dict()

    # ouverture fichier
    myfile = open(filename, "r")

    chaine = myfile.read()

    # separation des lignes
    listeLignes = chaine.splitlines()

    bg["map"] = []

    # transformation en liste de liste
    for line in listeLignes:
        listeChar = list(line)
        bg["map"].append(listeChar)

    myfile.close()

    bg["spawn"] = getSpawn(bg)
    bg["finish"] = getFinish(bg)

    return bg


def getSpawn(bg):

    spawn = None
    trouver = False

    for y in range(0, len(bg["map"])):
        for x in range(0, len(bg["map"][y])):
            if bg["map"][y][x] == "0":
                spawn = (y + 1, x + 1)
                trouver = True
                break
        if trouver:
            break

    return spawn


def setSpawn(bg):
    bg["spawn"] = getSpawn(bg)


def show(bg, win):
    for y in range(0, len(bg["map"])):
        for x in range(0, len(bg["map"][y])):

            # affiche le background
            win.addstr(y, x, bg["map"][y][x])


def getFinish(bg):

    finish = None
    trouver = False

    for y in range(0, len(bg["map"])):
        for x in range(0, len(bg["map"][y])):
            if bg["map"][y][x] == "F":
                finish = (y + 1, x + 1)
                trouver = True
                break
            if trouver:
                break

    return finish


def setFinish(bg):
    bg["finish"] = getFinish(bg)
