from battleship import *
import random

class ai(object):
    def __init__(self):
        
        self.game = board()
        self.xy = [0, 0]

    def put_ships(self):
        #Actual function to place ships, placeholder was pretty good
        randomCPU = self.getXY()
        
        #random v or h
        dir = random.randint(0, 1)
        if dir == 0:
            randomCPU.append('h')
        else:
            randomCPU.append('v')

        return randomCPU

    def attack(self, game, play):
        game.drawScreen()
        if game.p_map[self.xy[0]][self.xy[1]] == 3:
            #20% chance of cpu getting direct hit
            chance = random.randint(0, 4)
            if chance == 0:
                self.xy = self.findHuman()
                play.human_ships = game.battle(self.xy[0], self.xy[1], True, play.human_ships)
            else:
                self.xy = self.fireBlind()
                play.human_ships = game.battle(self.xy[0], self.xy[1], True, play.human_ships)               
                
        while True:
            self.xy = self.getXY()
            if game.p_map[self.xy[0]][self.xy[1]] in (0, 1):
                play.human_ships = game.battle(self.xy[0], self.xy[1], True, play.human_ships)
                break
                

    def getXY(self):
        return [random.randint(0, (self.game.X_AXIS-1)), random.randint(0, (self.game.Y_AXIS-1))]

        
    def findHuman(self):
        #9 o'clock
        if game.p_map[(self.xy[0]-1)][self.xy[1]] == 1:
            return [(self.xy[0]-1),self.xy[1]]
        #12 o'clock
        if game.p_map[self.xy[0]][(self.xy[1]-1)] == 1:
            return [self.xy[0],(self.xy[1]-1)]
        #3 o'clock
        if game.p_map[(self.xy[0]+1)][self.xy[1]] == 1:
            return [(self.xy[0]+1),self.xy[1]]
        #6 o'clock
        if game.p_map[self.xy[0]][(self.xy[1]+1)] == 1:
            return [self.xy[0],(self.xy[1]+1)]

    def fireBlind(self):
        side = random.randint(0, 3)
        if side == 0:
            return [(self.xy[0]-1),self.xy[1]]
        if side == 1:
            return [self.xy[0],(self.xy[1]-1)]
        if side == 2:
            return [(self.xy[0]+1),self.xy[1]]
        if side == 3:
            return [self.xy[0],(self.xy[1]+1)]