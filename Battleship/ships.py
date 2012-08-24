#using mutable types for returns 
#ship class takes in xy coordinates and direction and returns ship object
#coordinate verification must be near or in user input
class fiveSquareShip(object):
    def __init__(self, x, y, dir):
        self.info = {'size': 5, 'x': x, 'y': y, 'direction': dir}

    def getSize(self):
        return self.info['size']

    def getDirection(self):
        return self.info['direction']

    def getXY(self):
        return self.info['x'], self.info['y']

class fourSquareShip(object):
    def __init__(self, x, y, dir):
        self.info = {'size': 4, 'x': x, 'y': y, 'direction': dir}
    
    def getSize(self):
        return self.info['size']

    def getDirection(self):
        return self.info['direction']

    def getXY(self):
        return self.info['x'], self.info['y']


class threeSquareShip(object):
    def __init__(self, x, y, dir):
        self.info = {'size': 3, 'x': x, 'y': y, 'direction': dir}

    def getSize(self):
        return self.info['size']
    
    def getDirection(self):
        return self.info['direction']

    def getXY(self):
        return self.info['x'], self.info['y']
        