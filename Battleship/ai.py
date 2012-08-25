from battleship import *
import random

class ai(object):
    def __init__(self):
        
        game = board()

    def put_ships(self):
        x = random.randint(1, game.X_AXIS+1)
        y = random.randint(1, game.Y_AXIS+1)
        
        #random v or h
        dir = random.randint(0, 1)
        if dir == 0:
            dir = 'h'
        else:
            dir = 'v'
        return '%d, %d, %s' % (x, y, dir)
        