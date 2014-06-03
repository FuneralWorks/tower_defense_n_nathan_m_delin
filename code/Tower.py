import logging


def set(player):
    test = testTower(player)
    if player['money'] >= 50 and test is False:
        player['towerList'].append(player['pos'])
        player['money'] -= 50


def show(player, win):
    for a in range(1, len(player["towerList"])):
        win.addch(player["towerList"][a][1], player["towerList"][a][0], "T")


def shoot(level, player, n):
    monster = level['horde'][n]
    pos = (monster['x']-1, monster['y']-1)
    for a in range(0, len(player['towerList'])):
        if pos[0] == player['towerList'][a][0]-1 and pos[1] == player['towerList'][a][1]:
            monster['life'] -= 1
        elif pos[0] == player['towerList'][a][0]+1 and pos[1] == player['towerList'][a][1]:
            monster['life'] -= 1
        elif pos[0] == player['towerList'][a][0] and pos[1]-1 == player['towerList'][a][1]:
            monster['life'] -= 1
        elif pos[0] == player['towerList'][a][0] and pos[1]+1 == player['towerList'][a][1]:
            monster['life'] -= 1


def testTower(player):
    test = False
    for n in range(0, len(player['towerList'])):
        if player['pos'] == player['towerList'][n][0]:
            logging.info(player['towerList'][n][0])
            test = True
    return test
