

def set(player):
    if player['money'] >= 50:
        player['towerList'].append(player['pos'])
        player['money'] -= 50


def show(player, win):
    for a in range(1, len(player["towerList"])):
        win.addch(player["towerList"][a][1], player["towerList"][a][0], "T")


def shoot(level, player):
    monster = level['horde'][0]
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
