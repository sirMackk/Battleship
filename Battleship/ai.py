from battleship import *
import random

class ai(object):
    def __init__(self):
        
        self.game = board()

    def put_ships(self):
        #PLACE HOLDER FUNCTION TO TEST OUT PLAYGAME.PY
        randomCPU = []
        x = random.randint(0, (self.game.X_AXIS-1))
        y = random.randint(0, (self.game.Y_AXIS-1))
        randomCPU.append(x)
        randomCPU.append(y)
        
        #random v or h
        dir = random.randint(0, 1)
        if dir == 0:
            dir = 'h'
        else:
            dir = 'v'
        randomCPU.append(dir)
       # print x, y, dir
        return randomCPU
        #return '%d, %d, %s' % (x, y, dir)

    def attack(self, game, play):
        game.drawScreen()
       # input = False
        while True:
            x = random.randint(0, (game.X_AXIS-1))
            y = random.randint(0, (game.Y_AXIS-1))
            if game.p_map[x][y] not in (2, 3, 4):
                play.human_ships = game.battle(x, y, True, play.human_ships)
                break

        
        