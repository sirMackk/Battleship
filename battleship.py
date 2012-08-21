import random



def drawScreen(playerMap, computerMap):
    #code for drawing map
    #print player map first on left hand side
    #then the computer on the right side. works kinda like a typewriter, using arrays for coordinates
    topScreen()
    for i in range(0, 15):
        if i > 8:
            yaxis = 3
        else:
            yaxis = 4
        #draw human y axis
        mapy = '%s%d' % (' ' * yaxis, i+1)
    #loop for y axis
        for j in range(0, 25):
        #loop for x axis
            if playerMap[j][i] == 1:
                mapy += 'U'
            elif playerMap[j][i] == 2:
                mapy += 'O'
            elif playerMap[j][i] == 3:
                mapy += 'H'
            elif playerMap[j][i] == 4:
                mapy += 'S'
            else:
                mapy += oceanSign()
    #make space
        if i > 8:
            mapy += ' ' * 18
        else:
            mapy += ' ' * 19
        #draw computer y axis
        mapy += '%d' % (i+1)
        for j in range(0, 25):
            if computerMap[j][i] == 2:
                mapy += 'O'
            elif computerMap[j][i] == 3:
                mapy += 'H'
            elif computerMap[j][i] == 4:
                mapy += 'S'
            else:  
                mapy += oceanSign()
        print mapy
      #  mapy = ' ' * 5
    
    print '%sLegend: U - your ship, O - miss, H - hit, S - sunk' % (' ' * 12)

def oceanSign():
    if random.randint(0, 1) == 0:
        return '~'
    else:
        return "'"

def topScreen():
    print '\n\n'
    print '%sHuman%sComputer' % (' ' * 5, ' ' * 40)
    #draw x axis above boards
    print '%s1%s2%s1%s2' % (' ' * 14, ' ' * 9, ' ' * 34, ' ' * 9)
    print '%s1234567890123456789012345%s1234567890123456789012345' % (' ' * 5, ' ' * 20)


pMap = [[0 for i in range(0, 15)] for i in range(0, 25)]
cMap = [[0 for i in range(0, 15)] for i in range(0, 25)]
drawScreen(pMap, cMap)

pMap[18][2] = 1
cMap[18][5] = 1
drawScreen(pMap, cMap)

print '\n\n'
raw_input('Please enter coordinates to nuke: ')