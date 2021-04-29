from math import sqrt


class Airplane:
    """
    consumption: an integer representing number of litres consumed per km of distance

    position: a tuple (pair) of integers representing a position of the plane on a map
    (assume that the airplane can only be in one of the positions of the 1 km x 1 km grid)

    fuel_level: a float number representing the current fuel level in litres.
    """
    def __init__(self, initX, initY, cons, init_fuel):
        self.position = (initX, initY)
        self.cons = cons
        self.fuel_level = init_fuel

    def goto(self, X, Y):
        required_fuel = sqrt(((X - self.position[0]) ** 2) + ((Y - self.position[1]) ** 2))
        required_fuel = required_fuel * self.cons
        if required_fuel > self.fuel_level:
            return False
        else:
            self.position = (X, Y)
            self.fuel_level -= required_fuel
            return True

    def refuel(self, fuel):
        self.fuel_level += fuel



ap789 = Airplane(0, 0, 10, 3000)
assert ap789.goto(95,70) == True
assert ap789.position[0] == 95 and ap789.position[1] == 70
assert abs(ap789.fuel_level - 1819.96) < 0.01
assert ap789.goto(300,300) == False
assert abs(ap789.fuel_level - 1819.96) < 0.01