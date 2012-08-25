from battleship import *
from ships import *
from ai import *

class playgame(object):
    #start
    #human place ships
    def __init__(self, game):

        self.SHIPS = {'fiveSquareShip': 1, 'fourSquareShip': 3, 'threeSquareShip': 4}
        #show some welcome screen here
        
        #this creates the board and draws it
        self.game = game
        game.drawScreen()


    def human_start(self):
        human_ships = []
        self.human_ships = []
        for i in range(len(self.SHIPS)):
            human_ships.append(self.put_ship(self.SHIPS, i, True))
        for i in range(len(human_ships)):
            for j in range(len(human_ships[i])):
                self.human_ships.append(human_ships[i][j])

    def computer_start(self):
        computer_ships = []
        self.computer_ships = []
        for i in range(len(self.SHIPS)):
            computer_ships.append(self.put_ship(self.SHIPS, i, False))
        for i in range(len(computer_ships)):
            for j in range(len(computer_ships[i])):
                self.computer_ships.append(computer_ships[i][j])
        
    def put_ship(self, ships, iter, player):
        temp_list = []

        for i in range(ships.value()[iter]):
            the_ship = False
            while the_ship == False:
                humanXY = False
                #do if human - run this, else, run AI ship placement from ai.py
                while humanXY == False:
                    if player == True:
                        game.drawScreen()
                        humanXY = self.verify_input(raw_input("Enter coordinates to place 3 square ship eg. x,y, h(orizontal)/v(verticle)\n"))
                        print humanXY
                    else:
                        #work in progress
                        humanXY = ai.put_ships()

                direction = {'h': 'horizontal', 'v': 'verticle'}
                the_ship = (game.placeShip(ships.keys()[iter]((humanXY[0], humanXY[1], direction[humanXY[2]]), player))  
                #original function
                # the_ship = (game.placeShip(threeSquareShip(humanXY[0], humanXY[1], #direction[humanXY[2]]), player))
            print 'bla'
            temp_list.append(the_ship)
        return temp_list

    def verify_input(self, input):
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
                verify[0] = int(verify[0])-1
        except ValueError:
                    return False
        try:       
            if int(verify[0]) in range(0, game.Y_AXIS):
                verify[1] = int(verify[1])-1
        except ValueError:
                return False
        verify[2].lower()
        if verify[2] != 'v' and verify[2] != 'h':
                return False
        

#MAIN GAME LOOP:

while True:
    game = board()
    game.drawScreen()
    play = playgame(game)
    play.human_start()
    play.computer_start()
    input()
    game.drawScreen()
    input()




    ##main game loop
    #random player starts
    #other player plays
    #wanna play again?

#make tests for this too