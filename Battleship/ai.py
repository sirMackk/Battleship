from battleship import *
import random

class ai(object):
    def __init__(self):
        
        self.game = board()

    def put_ships(self):
        #PLACE HOLDER FUNCTION TO TEST OUT PLAYGAME.PY
        randomCPU = []
        x = random.randint(1, self.game.X_AXIS+1)
        y = random.randint(1, self.game.Y_AXIS+1)
        randomCPU.append(x)
        randomCPU.append(y)
        
        #random v or h
        dir = random.randint(0, 1)
        if dir == 0:
            dir = 'h'
        else:
            dir = 'v'
        randomCPU.append(dir)
        return randomCPU
        #return '%d, %d, %s' % (x, y, dir)
        