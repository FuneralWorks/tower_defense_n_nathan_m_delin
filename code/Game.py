import curses
import logging
import Animat
import Background
import Player
import Tower
import time


def create(background, player, level, win, refTime):

    return {
        'player': player,
        'level': level,
        'background': background,
        'win': win,
        'refTime': refTime
    }


def getCursor(player):
    return player['pos'][0], player['pos'][1]


def setCursor(player, newPos):
    player['pos'] = newPos
    return player['pos']


def showCursor(player, win):
    win.addstr(player['pos'][1], player['pos'][0], 'x')


def interact(game, numMonster):
    #logging.info("Num munster : "+str(numMonster))
    win = getWin(game)
    player = getPlayer(game)
    bg = getBackground(game)
    level = getLevel(game)
    refTime = game['refTime']
    gameTime = int(time.time())

    win.timeout(0)
    key = win.getch()
    cursorMove(player, bg, win, key)

    if gameTime - refTime == 1:
        #logging.info("DEBUG")
        for n in range(0, len(level['horde'])):
            #logging.info('n : '+str(n))
            if level['horde'][n]['mvt'] is True:
                    #logging.info('monster '+str(n))
                    move(game, level['horde'][n])
        if numMonster < len(level['horde']):
            level['horde'][numMonster]['mvt'] = True
            numMonster += 1

        game['refTime'] = gameTime
        for nMonster in range(len(level['horde'])):
            Tower.shoot(level, player, nMonster)

    return numMonster


def cursorMove(player, bg, win, key):
    pos = getCursor(player)

    x = pos[0]
    y = pos[1]

    # if key == curses.KEY_UP or curses.KEY_DOWN or curses.KEY_RIGHT or
    # curses.KEY_LEFT :

    if key == curses.KEY_UP and pos[1] > 1:
        y -= 1

    elif key == curses.KEY_DOWN and pos[1] < len(bg["map"]) - 1:
        y += 1

    elif key == curses.KEY_RIGHT and pos[0] < len(bg["map"][pos[1]]) - 1:
        x += 1

    elif key == curses.KEY_LEFT and pos[0] > 1:
        x -= 1

    pos = (x, y)
    player['pos'] = setCursor(player, pos)

    if key == ord('a'):
        Tower.set(player)


def show(game):
    win = getWin(game)
    bg = getBackground(game)
    level = getLevel(game)
    player = getPlayer(game)

    win.erase()

    Background.show(bg, win)
    showCursor(player, win)
    for n in range(0, len(level['horde'])):
        Animat.show(level['horde'][n], win)
    Player.show(player, win)
    Tower.show(player, win)


def getPos(monster):

    pos = monster["y"] - 1, monster["x"] - 1
    return pos


def move(game, monster):
    bg = getBackground(game)
    player = getPlayer(game)

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

    elif monster['life'] == 0:
        gainKill(player)


def perteVie(monster, bg, player, pos):
    if bg["map"][pos[0]][pos[1] + 1] == 'F':
        monster["x"] += 1
        player["life"] -= 1


def gainKill(player):
    player['money'] += 50
    return player['money']


def getWin(game):

    return game['win']


def getLevel(game):
    return game['level']


def getPlayer(game):
    return game['player']


def getBackground(game):
    return game['background']
