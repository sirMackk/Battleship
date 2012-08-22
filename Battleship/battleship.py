import random

#TODO - make mutator functions for the board game
#     - an interface to place ships along with rotation
#     - game interface
#     - make runner class that runs the game
#     - make interface class that gives a connections between player and board
#     - WORK ON SHIP PLACEMENT FUNCTION
#     - WORK ON isFree FUNCTION
class board(object):

    def __init__(self):
        
        self.y_axis = 15
        self.x_axis = 25
        self.p_map = [[0 for i in range(self.y_axis)] for i in range(self.x_axis)]
        self.c_map = [[0 for i in range(self.y_axis)] for i in range(self.x_axis)]


    def drawScreen(self):
        #code for drawing map
        #print player map first on left hand side
        #then the computer on the right side. works kinda like a typewriter, using arrays for coordinates
        self.topScreen()
        for i in range(0, self.y_axis):
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
            for j in range(0, self.x_axis):

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
            
            for j in range(0, self.x_axis):
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
        if players[player] == 1:
             mapx += 'U'
        elif players[player] == 2:
            mapx += 'O'
        elif players[player] == 3:
            mapx += 'H'
        elif players[player] == 4:
            mapx += 'S'
        else:
            mapx += self.oceanSign()
      #  self.player = not self.player
        
        return mapx

    # def placeShip(self, x, y, size, direction, player):
         ##   copies the maps for collision detection
            # temp_p_map = [self.p_map[i] for i in range(self.xaxis)]
            # temp_c_map = [self.c_map[i] for i in range(self.xaxis)]
        ##    true - human, false - computer
            # players = {True: temp_p_map[x][y], False: temp_c_map[x][y]}
           ## True is horizontal, False is verticle
            # if direction == True: 
                # for i range(size):
               ##     use ifFree function here
                    # if players[player] == 4 and:
                        # return 'There\'s a sunk ship here'


    def isFree(self, x, y, player):


#THIS FUNCTIONS NEEDS WORK, IT AINT WORKING RIGHT
#ONLY REPORTS x,y obstacle, DOES NOT CHECK AROUND x, y

        temp_p_map = [self.p_map[i] for i in range(self.x_axis)]
        temp_c_map = [self.c_map[i] for i in range(self.x_axis)]
        #true - human, false - computer
        i = 0; j = 0
        players = {True: temp_p_map[x+j][y+i], False: temp_c_map[x+j][y+i]}
        or_x = x
        or_y = y
        #checks to see if there's a free square of space around a ship
        #must be careful for out of index errors for lists
        #these checks do this - take in a copy of x y coordinates, compare them to a copy of
        #a map, then they check all spaces around them for free space. The for loops in these checks
        #either take away or add x or y coordinates for the checking routine.

        #following code can be much improved upon using elifs or maybe another function
        #checks upper right corner, if there's something in the way - returns false
        if or_x == 0 and or_y == 0:
            for i in [0, 1]:
                for j in [0, 1]:
                    if players[player] == 1:
                        return False

        #checks upper row
        if or_x != 24 and or_y == 0:
            for i in [0, 1]:
                for j in [-1, 0, 1]:
                    if players[player] == 1:
                        return False

        #checks upper right corner
        if or_x == 24 and or_y == 0:
            for i in [0, 1]:
                for j in [-1, 0]:
                    if players[player] == 1:
                        return False

        #checks bottom left corner:
        if or_x == 0 and or_y == 14:
            for i in [-1, 0]:
                for j in [0, 1]:
                    if players[player] == 1:
                        return False
        #check bottom row:
        if or_x != 24 and or_y == 14:
            for i in [-1, 0]:
                for j in [-1, 0, 1]:
                    if players[player] == 1:
                        return False
        #check bottom right corner:
        if or_x == 24 and or_y == 14:
            for i in [-1, 0]:
                for j in [-1, 0]:
                    if players[player] == 1:
                        return False
        #check left hand column:
        if or_x == 0:
            for i in [-1, 0, 1]:
                for j in [0, 1]:
                    if players[player] == 1:
                        return False
        #check right column:
        if or_x == 24:
            for i in [-1, 0, 1]:
                for j in [-1, 0]:
                    if players[player] == 1:
                        return False
        #not near corners or edges
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if players[player] == 1:
                    return False
        #if none of these tests already returned False, it means area if free for placing a ship
        #return true

        return True
                
            
        
        
                    
                
        
            


#simple test code
game = board()
game.p_map[5][12] = 1
game.p_map[5][11] = 1
game.p_map[6][11] = 1
game.drawScreen()
game.drawScreen()

# pMap[18][2] = 1
# cMap[18][5] = 1
# drawScreen(pMap, cMap)

print '\n\n'
raw_input('Please enter coordinates to nuke: ')
print game.isFree(5, 10, True)
print game.isFree(5, 11, True)
print game.isFree(0, 0, True)