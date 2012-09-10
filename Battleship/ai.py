from battleship import *
import random

class ai(object):
    def __init__(self):
        
        self.game = board()
        self.xy = [0, 0]
        self.moves = []

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
        #dont need to draw screen here
        #game.drawScreen()
        print self.moves
        self.moves.append(self.xy)
        if game.p_map[self.xy[0]][self.xy[1]] == 3:
            #25% chance of cpu getting direct hit
           # chance = random.randint(0, 3)
            chance = 0
            if chance == 0:
                self.xy = self.findHuman(game)

                play.human_ships = game.battle(self.xy[0], self.xy[1], True, play.human_ships)
            else:
                print self.xy
                #xy = self.xy
                while True:
                    self.xy = self.fireBlind(game)
                    if self.xy[0] in range(game.X_AXIS) and self.xy[1] in range (game.Y_AXIS):
                        break

                play.human_ships = game.battle(self.xy[0], self.xy[1], True, play.human_ships)
                if game.p_map[self.xy[0]][self.xy[1]] == 2:
                #    self.xy = xy
                    self.xy = self.moves[len(self.moves)-1]
        else:              
            while True:
                self.xy = self.getXY()
                if self.game.p_map[self.xy[0]][self.xy[1]] in (0, 1):
                    play.human_ships = game.battle(self.xy[0], self.xy[1], True, play.human_ships)
                    break
                

    def getXY(self):
        return [random.randint(0, (self.game.X_AXIS-1)), random.randint(0, (self.game.Y_AXIS-1))]

        
    def findHuman(self, game):
        i = 1
        while True:
            #9 o'clock
            print self.xy
            print game.p_map[(self.xy[0]-1)][self.xy[1]], (self.xy[0]-1),self.xy[1]
            if game.p_map[(self.xy[0]-1)][self.xy[1]] == 1:
                return [(self.xy[0]-1),self.xy[1]]
            #12 o'clock
            print self.game.p_map[self.xy[0]][(self.xy[1]-1)], self.xy[0],(self.xy[1]-1)
            if game.p_map[self.xy[0]][(self.xy[1]-1)] == 1:
                return [self.xy[0],(self.xy[1]-1)]
            #3 o'clock
            print game.p_map[(self.xy[0]+1)][self.xy[1]], (self.xy[0]+1),self.xy[1]
            if game.p_map[(self.xy[0]+1)][self.xy[1]] == 1:
                return [(self.xy[0]+1),self.xy[1]]
            #6 o'clock
            print game.p_map[self.xy[0]][(self.xy[1]+1)], self.xy[0],(self.xy[1]+1)
            if game.p_map[self.xy[0]][(self.xy[1]+1)] == 1:
                return [self.xy[0],(self.xy[1]+1)]
            self.xy = self.moves[(len(self.moves)-i)]
            i += 1
            

    def fireBlind(self, game):
        while True:
            side = random.randint(0, 3)
            #dont allow double misses
            if side == 0 and self.xy[0] > 0 and game.p_map[(self.xy[0]-1)][self.xy[1]] not in (2,3):
                return [(self.xy[0]-1),self.xy[1]]
            if side == 1 and self.xy[1] > 0 and game.p_map[self.xy[0]][(self.xy[1]-1)] not in (2,3):
                return [self.xy[0],(self.xy[1]-1)]
            if side == 2 and self.xy[0] < (game.X_AXIS-1) and game.p_map[(self.xy[0]+1)][self.xy[1]] not in (2,3):
                return [(self.xy[0]+1),self.xy[1]]
            if side == 3 and self.xy[1] < (game.Y_AXIS-1) and game.p_map[self.xy[0]][(self.xy[1]+1)] not in (2,3):
                return [self.xy[0],(self.xy[1]+1)]