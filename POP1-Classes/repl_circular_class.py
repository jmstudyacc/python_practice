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
        inter_sector = Sector()
        inter_sector.fr = max(self.fr, other.fr)
        inter_sector.to = min(self.to, other.to)
        inter_sector.rad = min(self.rad, other.rad)

        return f"{inter_sector.fr} {inter_sector.to} {inter_sector.rad}"
        # implement this
        # returns sector (i.e., object of class Sector) that is intersection
        # of this and other sector
        # you may assume that the two sectors have nonempty intersection

    def is_empty(self):
        # why do I need to search for geometry formulae?
        # why is this part of programming/testing classes?!
        # Sector Area = r^2 * angle / 2
        # s1 = 40^2 * 20 / 2 ?

        total_angle = self.to - self.fr
        sector_area = (self.rad ** 2 * total_angle) / 2

        if sector_area != 0:
            return False
        else:
            return True

        # implement this
        # returns True if the sector has empty area, otherwise False

    def __eq__(self, other):
        if self.fr == other.fr and self.to == other.to and self.rad == other.rad:
            return True
        else:
            return False

        # implement this
        # returns True this sector is the same as the other, otherwise False

    def __str__(self):
        # implement this
        # returns string "F T R" where F is from angle, T is to, and R is radius
        return f"{self.fr} {self.to} {self.rad}"