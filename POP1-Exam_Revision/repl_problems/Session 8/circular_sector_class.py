class Sector:
    def __init__(self):
        self.fr = 0
        self.to = 0
        self.rad = 0

    def rotate(self, angle):
        # this rotates the sector by an angle
        pass

    def intersect(self, other):
        # returns sector, object of class Sector, that is intersection of this and another sector
        pass

    def is_empty(self):
        # returns True if the sector has empty area, else False
        pass

    def __eq__(self, other):
        # returns True if this sector is the same as the other, else False
        pass

    def __str__(self):
        # returns string F T R, F = angle, T = to, R = radius
        pass