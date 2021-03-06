from battleship import *
from ships import *
from ai import *
from random import randint

class playgame(object):
    #start
    #human place ships
    def __init__(self, game, ai):


        self.SHIPS = {fiveSquareShip: 2, fourSquareShip: 3, threeSquareShip: 4}
        #show some welcome screen here
        
        #this creates the board and draws it
        self.game = game
        game.drawScreen()
        self.ai = ai


    def human_start(self):
        human_ships = []
        self.human_ships = []
        for i in range(len(self.SHIPS)):
            human_ships.append(self.put_ship(self.SHIPS, i, True))
        for i in range(len(human_ships)):
            for j in range(len(human_ships[i])):
                self.human_ships.append(human_ships[i][j])
        #self.human_ships is a 1d list of ship objects
        #this function should return the human_ships list as a way to track health
      #  return self.human_ships

    def computer_start(self):
        computer_ships = []
        self.computer_ships = []
        for i in range(len(self.SHIPS)):
            computer_ships.append(self.put_ship(self.SHIPS, i, False))
        for i in range(len(computer_ships)):
            for j in range(len(computer_ships[i])):
                self.computer_ships.append(computer_ships[i][j])
        #testing
#return self.computer_ships
        
    def put_ship(self, ships, iter, player):
        temp_list = []
        direction = {'h': 'horizontal', 'v': 'verticle'}
        for i in range(ships.values()[iter]):

            humanXY = False
                #do if human - run this, else, run AI ship placement from ai.py
            while humanXY == False:
                if player == True:
                    while humanXY == False:
                        game.drawScreen()
                        humanXY = self.verify_input(raw_input("Enter coordinates to place a ship eg. x,y, h(orizontal)/v(verticle)\n" ), True)
                        
                else:
                        
                        #work in progress

                    humanXY = self.ai.put_ships()

                #bug here : if ship cannot be placed due to other ship close by
                #then shipp will be added to list of ship objects
                #the loop will iterate, but ship wont be added to map
                #FIXED ABOVE BUG

                the_ship = ships.keys()[iter](humanXY[0], humanXY[1], direction[humanXY[2]])
                if game.placeShip(the_ship, player) == False:
                    humanXY = False

            
            temp_list.append(the_ship)
        return temp_list

    def verify_input(self, input, battle):
            #update this function so it can handle both ship placement input
            #as well as battle input
            #UPDATE: Done as above. battle==true for ship placement, false for battle

            #split into list
        verify = input.split(',')
        
        if len(verify) < 3 and battle == True and verify != False:
            return False
        elif len(verify) < 2 and battle == False and verify != False:
            return False
            #remove leading and trailing whitespaces
        for i in range(len(verify)):
                verify[i] = verify[i].strip()
        
            #verify if first two items are numbers and the third is either v or h
        try:
            if int(verify[0]) in range(1, (self.game.X_AXIS+1)):
                verify[0] = int(verify[0])-1
            else:
                return False
        except ValueError:
                    return False
        try:       
            if int(verify[1]) in range(1, (self.game.Y_AXIS+1)):
                verify[1] = int(verify[1])-1
            else:
                return False
        except ValueError:
                return False
        if battle == True:
            verify[2].lower()
            if verify[2] != 'v' and verify[2] != 'h':
                return False
        
        return verify

    def calcHealth(self, player):
        players = {True: self.human_ships, False: self.computer_ships}

        health = 0

        for i in range(len(players[player])):
            health += players[player][i].getHealth()

        return health
        
    def humanAttack(self):
        game.drawScreen()


        while True:
            human_fire = self.verify_input(raw_input('Enter coordinates to fire eg. x, y: '), False)
            if human_fire != False:
                if game.c_map[human_fire[0]][human_fire[1]] not in (2, 3, 4):
                    self.computer_ships = game.battle(human_fire[0], human_fire[1], False, self.computer_ships)
                    break
    
#MAIN GAME LOOP:

while True:
    game = board()
    computer = ai()
    play = playgame(game, computer)
    play.computer_start()
    play.human_start()
    while play.calcHealth(True) > 0 and play.calcHealth(False) > 0:
        play.humanAttack()
        computer.attack(game, play)
        print "Human health: %d \nComputer health: %d" % (play.calcHealth(True), play.calcHealth(False))
        
