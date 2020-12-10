class Sector:
    def __init__(self):
        self.fr = 0
        self.to = 0
        self.rad = 0

    def rotate(self, angle):
        self.fr += angle
        self.to += angle
        # implement this
        # rotates sector by angle
        # you man assume the rotation never results in a sector with fr > to
        # (it is optional to solve this problem without this assumption; see above)

    def intersect(self, other):
        pass
        # implement this
        # returns sector (i.e., object of class Sector) that is intersection
        # of this and other sector
        # you may assume that the two sectors have nonempty intersection

    def is_empty(self):
        pass
        # implement this
        # returns True if the sector has empty area, otherwise False

    def __eq__(self, other):
        # implement this
        # returns True this sector is the same as the other, otherwise False
        if self.fr == other.fr and self.to == other.to and self.rad == other.rad:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.fr} {self.to} {self.rad}"
        # implement this
        # returns string "F T R" where F is from angle, T is to, and R is radius


s1 = Sector()
s1.fr = 0
s1.to = 20
s1.rad = 40
str(s1)
s1.rotate(50)
print(str(s1))
s2 = Sector()
s2.fr = 60
s2.to = 100
s2.rad = 30
print(str(s2))

# s3 = s1.intersect(s2)
# Test4 checks str(s3)=="60 70 30"

new_sect = Sector()
new_sect.fr = max(self.fr, other.fr)
new_sect.to = min(self.to, other.to)
new_sect.rad = min(self.rad, other.rad)