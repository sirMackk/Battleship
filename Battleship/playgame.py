from battleship import *
from ships import *

class PlayGame(object):
    #start
    #human place ships
    def __init__(self):
        self.NUM_5_SQ_SHIP = 1
        self.NUM_4_SQ_SHIP = 3
        self.NUM_3_SQ_SHIP = 4
        #show some welcome screen here
        self.game = board()
        game.drawScreen()

    def human_put_ship(self):
        humanShips = []
    

    #placing a ship, defined by what type and how many of them
    #can optimize this further hell yeah, like making the for-loops a stand alone function
    #or by having one function for both player and computer to place ships
    for i in range(3):
        the_ship = False
        while the_ship == False:
            humanXY = False
            while humanXY == False:
                game.drawScreen()
                humanXY = verify_input(raw_input("Enter coordinates to place 3 square ship eg. x,y, h(orizontal)/v(verticle)\n"))
                print humanXY
            direction = {'h': 'horizontal', 'v': 'verticle'}
                    
            the_ship = (game.placeShip(threeSquareShip(humanXY[0], humanXY[1], direction[humanXY[2]]), True))
        humanShips.append(the_ship)

    def verify_input(input):
            #split into list
        verify = input.split(',')
        if len(verify) < 3:
            return False
            #remove leading and trailing whitespaces
        for i in range(len(verify)):
                verify[i] = verify[i].strip()

            #verify if first two items are numbers and the third is either v or h
        try:
            if int(verify[0]) in range(0, game.X_AXIS):
                verify[0] = int(verify[0])
        except ValueError:
                    return False
        try:       
            if int(verify[0]) in range(0, game.Y_AXIS):
                verify[1] = int(verify[1])
        except ValueError:
                return False
        verify[2].lower()
        if verify[2] != 'v' and verify[2] != 'h':
                return False
        
    #computer place ships
    ##main game loop
    #random player starts
    #other player plays
    #wanna play again?

#make tests for this too