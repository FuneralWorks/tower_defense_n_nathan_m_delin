import curses


def create(direction, x, y, cara, finishx, finishy, color, life, mvt):

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
    animat['mvt'] = mvt

    return animat


def show(monster, win):
    x = monster["x"] - 1
    y = monster["y"] - 1
    cara = monster["cara"]
    color = colorMonster(monster)
    curses.init_pair(1, color, -1)
    if monster['life'] > 0:
        win.addch(y, x, cara, curses.color_pair(1))


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
