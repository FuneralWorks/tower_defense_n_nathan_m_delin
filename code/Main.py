import curses
import time
import logging
# nos modules
import Background
import Game
import Player
import Level


def init():

    curses.initscr()
    curses.noecho()
    curses.cbreak()
    logging.basicConfig(filename = 'tower.log', level = logging.INFO)
    # definition de la fenetre
    begin_x = 0
    begin_y = 0
    height = 100
    width = 100
    win = curses.newwin(height, width, begin_y, begin_x)

    win.keypad(1)
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    # creation des elements du jeu
    background = Background.create("image.txt")
    player = Player.create(4, 1, 10, [(0, 0)], 200)
    level = Level.create(6, [], background, 5)
    refTime = int(time.time())
    game = Game.create(background, player, level, win, refTime)
    return game


def show(game):

    # affichage des different element
    Game.show(game)


def interact(game, numMonster):

    return Game.interact(game, numMonster)


def run(game):
    numMonster = 0
    # Boucle de simulation
    while 1:

        numMonster = interact(game, numMonster)
        #logging.info("numMonster Interact "+str(numMonster))
        #move(game)
        show(game)

game = init()
run(game)
