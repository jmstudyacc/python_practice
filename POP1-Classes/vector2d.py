import math
import matplotlib


class Vector2d:

    _x = None
    _y = None

    # We need to build a constructor when dealing with classes!
    def __init__(self, x=0, y=0):   # (1) adding the x & y variables to the class (2) adding default values
        self._x = x
        self._y = y

        # you need to create private variables only accessible inside the class
        # this is achieved with an underscore + variable e.g. _x

    def scale_update(self, c):
        """
        mutates and scales the Vector2d by multiplying coordinates by c

        Args:
            c: int

        Returns:
            coordinates showing the x & y values scaled by c
        """
        # maintain aspect ratio by scaling both _x and _y
        self._x *= c
        self._y *= c

        # (4) at present this method is a non-fruitful method
        # this method is mutating the object in place - not creating a new object

    def scale_fruitful(self, c):
        """
        returns a Vector2d (fruitful) by multiplying coordinates by c
        Args:
            c: int

        Returns:
            returns new coordinates after multiplying by c
        """
        # new variables are assigned to the value of local x variable multiplied by c
        new_x = self._x * c
        new_y = self._y * c

        # returns the result of Vector2d using new_x & new_y values
        return Vector2d(new_x, new_y)

    # requirement to calculate the distance between 2D vectors
    def distance_to(self, other):
        # provides the distance between two points using Math module
       return math.sqrt(
           (self._x - other._x) ** 2 +
           (self._y - other._y) ** 2)

    # adding coordinates of 1 vector to another
    def add(self, other):
        """
        Args:
            other: Vector2D

        Returns:
            returns a new 2D vector after adding the respective coordinates of self & other 2D vector
        """
        return Vector2d(self._x + other._x, self._y + other._y)

    # this next method will change how Python handles the keyword 'add'
    # this changes the binary operator between 2 objects
    def __add__(self, other):
        """
        overrides "+" operator and returns new 2dVector after adding respective coordinates of self and other 2dVector
        Args:
            other: Vector2d

        Returns:
        """
        # this would call the add() method defined above
        return self.add(other)
        # return Vector2d(self._x + other._x, self._y + other._y)

if __name__ == '__main__':
    # (1) when the below is called instantiate the class - but it is missing x & y!
    v = Vector2d(0, 0)  # (2) now the values of 0 & 0 are bound to x & y
    v1 = Vector2d(2, 3)

    print(v)
    print(v1)


# v._x - is perfectly allowed in Python but convention dictates this is avoided

