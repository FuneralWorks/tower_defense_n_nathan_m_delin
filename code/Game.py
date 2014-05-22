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


def interact(game):
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
        Animat.move(level, bg, player)
        game['refTime'] = gameTime
        Tower.shoot(level, player)


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
        logging.info('4')


def show(game):
    win = getWin(game)
    bg = getBackground(game)
    level = getLevel(game)
    player = getPlayer(game)

    win.erase()

    Background.show(bg, win)
    showCursor(player, win)
    Animat.show(level, win)
    Player.show(player, win)
    Tower.show(player, win)


def move(game):
    bg = getBackground(game)
    level = getLevel(game)
    player = getPlayer(game)



def getWin(game):

    return game['win']


def getLevel(game):
    return game['level']


def getPlayer(game):
    return game['player']


def getBackground(game):
    return game['background']
