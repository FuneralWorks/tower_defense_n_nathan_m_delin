import curses


def create(direction, x, y, cara, finishx, finishy, color, life):

    # creation animat
    animat = dict()
    animat["direction"] = direction
    animat["x"] = x
    animat["y"] = y
    animat["cara"] = cara
    animat["finishx"] = finishx
    animat["finishy"] = finishy
    animat['color'] = color
    animat['life'] = life

    return animat


def show(level, win):
    monster = level['horde'][0]
    x = monster["x"] - 1
    y = monster["y"] - 1
    cara = monster["cara"]
    color = colorMonster(monster)
    curses.init_pair(1, color, -1)
    if monster['life'] > 0:
        win.addch(y, x, cara, curses.color_pair(1))


def getPos(monster):

    pos = monster["y"] - 1, monster["x"] - 1
    return pos


def move(level, bg, player):
    monster = level['horde'][0]
    pos = getPos(monster)

    if bg["map"][pos[0]][pos[1] + 1] == '-' and monster["direction"] != "left":
        monster["x"] += 1
        monster["direction"] = "right"

    elif bg["map"][pos[0] + 1][pos[1]] == '-' and monster["direction"] != "up":
        monster["y"] += 1
        monster["direction"] = "down"

    elif bg["map"][pos[0]][pos[1] - 1] == '-' and monster["direction"] != "right":
        monster["x"] -= 1
        monster["direction"] = "left"

    elif bg["map"][pos[0] - 1][pos[1]] == '-' and monster["direction"] != "down":
        monster["y"] -= 1
        monster["direction"] = "up"
    elif monster['life'] > 0:
        perteVie(monster, bg, player, pos)


def colorMonster(monster):
    if monster['life'] == 4:
        monster['color'] = 2
    elif monster['life'] == 3:
        monster['color'] = 3
    elif monster['life'] == 2:
        monster['color'] = 1
    elif monster['life'] == 1:
        monster['color'] = 0
    return monster['color']


def perteVie(monster, bg, player, pos):
    if bg["map"][pos[0]][pos[1] + 1] == 'F':
        monster["x"] += 1
        player["life"] -= 1
