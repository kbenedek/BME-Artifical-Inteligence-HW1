class Car:
    def __init__(self, sizex, sizey, id):
        self.sizeX = sizex
        self.sizeY = sizey
        if id != 0:
            self.id = id
        else:
            raise Exception("Car ID cant be 0")

    def __repr__(self):
        return str(self.getId())

    def __str__(self):
        return self.getId()

    def __lt__(self, other):
        largestSelf = None
        if(self.sizeX > self.sizeY):
            largestSelf = self.sizeX
        else:
            largestSelf = self.sizeY
        largestOther = None
        if (other.sizeX > other.sizeY):
            largestOther = other.sizeX
        else:
            largestOther = other.sizeY
        return largestSelf < largestOther

    def getsizex(self):
        return self.sizeX

    def getsizey(self):
        return self.sizeY

    def rotate(self):
        tmp = self.sizeY
        self.sizeY = self.sizeX
        self.sizeX = tmp

    def getSize(self):
        return self.sizeY*self.sizeX

    def getId(self):
        return self.id
