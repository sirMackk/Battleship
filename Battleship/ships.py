#using mutable types for returns 
#ship class takes in xy coordinates and direction and returns ship object
#coordinate verification must be near or in user input
class fiveSquareShip(object):
    def __init__(self, x, y, dir):
        self.info = {'size': 5, 'x': x, 'y': y, 'direction': dir, 'health': 5}

    def getSize(self):
        return self.info['size']

    def getDirection(self):
        return self.info['direction']

    def getXY(self):
        return self.info['x'], self.info['y']

    def getHealth(self):
        return self.info['health']
    
    def getHit(self):
        self.info['health'] -= 1

class fourSquareShip(object):
    def __init__(self, x, y, dir):
        self.info = {'size': 4, 'x': x, 'y': y, 'direction': dir, 'health': 4}
    
    def getSize(self):
        return self.info['size']

    def getDirection(self):
        return self.info['direction']

    def getXY(self):
        return self.info['x'], self.info['y']

    def getHealth(self):
        return self.info['health']

    def getHit(self):
        self.info['health'] -= 1


class threeSquareShip(object):
    def __init__(self, x, y, dir):
        self.info = {'size': 3, 'x': x, 'y': y, 'direction': dir, 'health': 3}

    def getSize(self):
        return self.info['size']
    
    def getDirection(self):
        return self.info['direction']

    def getXY(self):
        return self.info['x'], self.info['y']

    def getHealth(self):
        return self.info['health']

    def getHit(self):
        self.info['health'] -= 1
        