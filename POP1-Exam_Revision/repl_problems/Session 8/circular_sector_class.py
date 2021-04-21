class Sector:
    def __init__(self):
        self.fr = 0
        self.to = 0
        self.rad = 0

    def rotate(self, angle):
        # this rotates the sector by an angle
        self.fr += angle
        self.to += angle

    def intersect(self, other):
        # returns sector, object of class Sector, that is intersection of this and another sector
        new_sector = Sector()
        new_sector.fr = max(self.fr, other.fr)
        new_sector.to = min(self.to, other.to)
        new_sector.rad = min(self.rad, other.rad)
        return new_sector

    def is_empty(self):
        # returns True if the sector has empty area, else False
        if abs(self.fr) - abs(self.to) == 0 or self.rad == 0:
            return True

        return False

    def __eq__(self, other):
        # this method will then be used to enable the == operator between 2 objects8
        if self.to == other.to and self.fr == other.fr and self.rad == other.rad:
            return True

        return False

    def __str__(self):
        # the method will be used to print the sector out like a typical string
        # returns string F T R, F = angle, T = to, R = radius
        return f"{self.fr} {self.to} {self.rad}"


# Checks str override
s1 = Sector()
s1.fr = 0
s1.to = 20
s1.rad = 40
print(s1)

# Checks rotate
s1.rotate(50)
print(s1)

# Checks equality
s2 = Sector()
s2.fr = 50
s2.to = 70
s2.rad = 40
print(s1 == s2)
s2.fr = 40
s2.to = 100
s2.rad = 30
print(s1 == s2)

# Checks intersection
s3 = s1.intersect(s2)
print(s3)