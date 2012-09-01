import random
from ships import *

#TODO - make mutator functions for the board game
#     - an interface to place ships along with rotation
#     - game interface
#     - make runner class that runs the game
#     - make interface class that gives a connections between player and board
#     - WORK ON SHIP PLACEMENT FUNCTION
#     - WORK ON isFree FUNCTION - DONE
#     - redo function and class names according to pep 8
class board(object):

    def __init__(self):
        
        self.Y_AXIS = 15
        self.X_AXIS = 25
        self.p_map = [[0 for i in range(self.Y_AXIS)] for i in range(self.X_AXIS)]
        self.c_map = [[0 for i in range(self.Y_AXIS)] for i in range(self.X_AXIS)]


    def drawScreen(self):
        #code for drawing map
        #print player map first on left hand side
        #then the computer on the right side. works kinda like a typewriter, using arrays for coordinates
        self.topScreen()
        for i in range(0, self.Y_AXIS):
            if i > 8:
                yaxis = 3
            else:
                yaxis = 4
            #draw human y axis
            mapy = '%s%d' % (' ' * yaxis, i+1)
            #loop for y axis
            #human = true
            #CLEAN THIS CODE TO MAKE IT READABLE TO AVOID EASY PROBLEMS
            player = True
            for j in range(0, self.X_AXIS):
            #loop for x axis
                mapy += self.drawOcean(player, j, i)

            player = not player
            #make space
            if i > 8:
                mapy += ' ' * 18
            else:
                mapy += ' ' * 19
            #draw computer y axis
            mapy += '%d' % (i+1)
            
            for j in range(0, self.X_AXIS):
                mapy += self.drawOcean(player, j, i)
            print mapy
        
        print '%sLegend: U - your ship, O - miss, H - hit, S - sunk' % (' ' * 12)

    def oceanSign(self):
        if random.randint(0, 1) == 0:
            return '~'
        else:
            return "'"

    def topScreen(self):
        print '\n\n'
        print '%sHuman%sComputer' % (' ' * 5, ' ' * 40)
        #draw x axis above boards
        print '%s1%s2%s1%s2' % (' ' * 14, ' ' * 9, ' ' * 34, ' ' * 9)
        print '%s1234567890123456789012345%s1234567890123456789012345' % (' ' * 5, ' ' * 20)
    #This function is responsible for drawing the human and cpu maps
    def drawOcean(self,player, j, i):
        players = {True: self.p_map[j][i], False: self.c_map[j][i]}
        mapx = ''

        if players[player] == 1 and player == True:
             mapx += 'U'
        elif players[player] == 2:
            mapx += 'O'
        elif players[player] == 3:
            mapx += 'H'
        elif players[player] == 4:
            mapx += 'S'
        else:
            mapx += self.oceanSign()

        
        return mapx

    def placeShip(self, ship, player):
        #this function will accept a ship object, unwrap the information from it
        #and use this information to place the ship on either human or computer board
        #it'll also use the isFree function to determine if ship can be placed there
        #and there will also be a routine to check if the ship doesnt go beyond the map

        #makes temporary copies of the maps, should return or modify originals at the end
        temp_p_map = [self.p_map[i] for i in range(self.X_AXIS)]
        temp_c_map = [self.c_map[i] for i in range(self.X_AXIS)]
        players = {True: temp_p_map, False: temp_c_map}
        players_real = {True: self.p_map, False: self.c_map}
        x, y = ship.getXY()
        size = ship.getSize()
        direction = ship.getDirection()

        

        if direction == 'horizontal' and x + size <= self.X_AXIS:
            mapa = self.placeHorizontal(x, y, size, players[player], player)
        elif direction == 'verticle' and y + size <= self.Y_AXIS:
            mapa = self.placeVerticle(x, y, size, players[player], player)
        else:
            #return false if ship is too big and cant place it or if there's another ship in the way
            return False

        if mapa != False:
            players_real[player] = mapa
        else:
            return False
        
    def placeHorizontal(self, x, y, size, map, player):
        for i in range(x, x+size):
            if self.isFree(i, y, player) == False:
                return False
        for i in range(x, x+size):
            map[i][y] = 1
        
        return map

    def placeVerticle(self, x, y, size, map, player):
        for i in range(y, y+size):
            if self.isFree(x, y, player) == False:
                return False
        for i in range(y, y+size):
            map[x][i] = 1

        return map
        
        


    def isFree(self, x, y, player):
    #usage : give x and y coordinates and the player for which to check if space is empty
    # true is human, false is computer - code will automagically pick correct board

        temp_p_map = [self.p_map[i] for i in range(self.X_AXIS)]
        temp_c_map = [self.c_map[i] for i in range(self.X_AXIS)]

        or_x = x
        or_y = y
        #checks to see if there's a free square of space around a ship
        #must be careful for out of index errors for lists
        #these checks do this - take in a copy of x y coordinates, compare them to a copy of
        #a map, then they check all spaces around them for free space. The for loops in these checks
        #either take away or add x or y coordinates for the checking routine.

        #following code can be much improved upon using elifs or maybe another function - DONE

        #checks upper right corner, if there's something in the way - returns false
        if or_x == 0 and or_y == 0:
            return self.isFreeSub(x, y, player, [0, 1], [0, 1], temp_p_map, temp_c_map)


        #checks upper row
        elif or_x != self.X_AXIS-1 and or_y == 0:
            return self.isFreeSub(x, y, player, [0, 1], [-1, 0, 1], temp_p_map, temp_c_map)

        #checks upper right corner
        elif or_x == self.X_AXIS-1 and or_y == 0:
            return self.isFreeSub(x, y, player, [0, 1], [-1, 0], temp_p_map, temp_c_map)


        #checks bottom left corner:
        elif or_x == 0 and or_y == self.Y_AXIS-1:
            return self.isFreeSub(x, y, player, [-1, 0], [0, 1], temp_p_map, temp_c_map)

        #check bottom right corner:
        elif or_x == self.X_AXIS-1 and or_y == self.Y_AXIS-1:
            return self.isFreeSub(x, y, player, [-1, 0], [-1, 0], temp_p_map, temp_c_map)
        

        #check bottom row:
        elif or_x != self.X_AXIS-1 and or_y == self.Y_AXIS-1:
            return self.isFreeSub(x, y, player, [-1, 0], [-1, 0, 1], temp_p_map, temp_c_map)



        #check left hand column:
        elif or_x == 0:
            return self.isFreeSub(x, y, player, [-1, 0, 1], [0, 1], temp_p_map, temp_c_map)

        #check right column:
        elif or_x == self.X_AXIS-1:
            return self.isFreeSub(x, y, player, [-1, 0, 1], [-1, 0], temp_p_map, temp_c_map)
        #not near corners or edges
        else:
            
            return self.isFreeSub(x, y, player, [-1, 0, 1], [-1, 0, 1], temp_p_map, temp_c_map)
        #if none of these tests already returned False, it means area if free for placing a ship

    
    def isFreeSub(self, x, y, player, xes, yes, temp_p_map, temp_c_map):
        #This function is a subrouting of the isFree function.
        #It basically makes sure not to duplicate a lot of for loops
        #xes and yes are the lists which contain the x, y coordinates
        #around a ship to see if the space around the ship is free.
        for i in xes:
            for j in yes:
                try:
                    players = {True: temp_p_map[x+j][y+i], False: temp_c_map[x+j][y+i]}
                    if players[player] == 1:                    
                        return False
                except IndexError:
                    #sometimes computer tries some wicked numbers and ai throws index error, gotta 
                    #check this out later, this is a temporary fix
                    print 'Index error: ', x, y, j, i
        return True
    
    def battle(self, x, y, player, ships):
        #xy - coordinates for attacking, player - True/False as usual, ships - list of ships from playgame.py
        #returns false if hit is bad ie. if hit is the same as previous hit, miss, or sunk
        #updates map when empty ocean - miss or updates map with good hit and calls health function
        #if health 0, then for loop should mark coordinates with sunk ship
        #maybe I should be working on copies of the main maps... but why?
        players = {True: self.p_map, False: self.c_map}

        if players[player][x][y] == 2 or players[player][x][y] == 3 or players[player][x][y] == 4:
            return ships, False
        elif players[player][x][y] == 0:
            players[player][x][y] = 2
            #return?
        else:
            #ship gets hit, loses hp and may become sunk
            return self.identify_ship(x, y, player, ships)
        return ships
        #should probably return list of ships
        #yeah, not returning list of ships caused error

    def identify_ship(self, x, y, player, ships):
        players = {True: self.p_map, False: self.c_map}
        for i in range(len(ships)):


            #we already know a ship has been hit, now we jsut gotta figure out which ship
            #it was.

            #horizontal check:
           # print ships
            print range(ships[i].getXY()[0], (ships[i].getXY()[0] + ships[i].getSize()))
            if ships[i].getDirection() == 'horizontal' and x in range(ships[i].getXY()[0], (ships[i].getXY()[0] + ships[i].getSize())) and y == ships[i].getXY()[1]:
                #optimize this part!
                ships[i].getHit()
                players[player][x][y] = 3
                print ships[i].getXY()
                self.isSunk(ships[i].getXY()[0], ships[i].getXY()[1], player, ships[i])
              #  break
            #verticle check:
            elif ships[i].getDirection() == 'verticle' and y in range(ships[i].getXY()[1], (ships[i].getXY()[1] + ships[i].getSize())) and x == ships[i].getXY()[0]:
                ships[i].getHit()
                players[player][x][y] = 3
                print 'balaaaaa'
                self.isSunk(ships[i].getXY()[0], ships[i].getXY()[1], player, ships[i])
              #  break
            
     

       
        
        return ships

    def isSunk(self, x, y, player, ship):   
        players = {True: self.p_map, False: self.c_map}
        if ship.getHealth() <= 0:
            if ship.getDirection() == 'horizontal':
                for i in range(ship.getXY()[0], (ship.getXY()[0] + ship.getSize())):
                    players[player][i][y] = 4
            else:
                for i in range(ship.getXY()[1], (ship.getXY()[1] + ship.getSize())):
                    players[player][x][i] = 4
        else:
            return False

                
        
    