import random

#TODO - make mutator functions for the board game
#     - an interface to place ships along with rotation
#     - game interface
class board(object):

    def __init__(self):
        
        self.y_axis = 15
        self.x_axis = 25
        self.p_map = [[0 for i in range(0, self.y_axis)] for i in range(0, self.x_axis)]
        self.c_map = [[0 for i in range(0, self.y_axis)] for i in range(0, self.x_axis)]


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
            for j in range(0, self.x_axis):

            #loop for x axis
                #human = true
                player = True
            
                mapy += self.drawOcean(player, j, i)
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
    def drawOcean(self, player, j, i):
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
            player = not player
        return mapx



game = board()
game.p_map[5][10] = 1
game.drawScreen()
# pMap[18][2] = 1
# cMap[18][5] = 1
# drawScreen(pMap, cMap)

print '\n\n'
raw_input('Please enter coordinates to nuke: ')