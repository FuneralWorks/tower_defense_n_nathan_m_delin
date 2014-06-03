

def create(x, y, life, towerList, money):
    player = dict()
    player['pos'] = (x, y)
    player["life"] = life
    player["towerList"] = towerList
    player['money'] = money

    return player


def show(player, win):
    showLife(player, win)
    showMoney(player, win)


def showLife(player, win):

    win.addstr(5, 40, " Vies : " + str(player["life"]) + " ")


def showMoney(player, win):
    win.addstr(6, 40, " Argent : " + str(player['money']) + " ")


