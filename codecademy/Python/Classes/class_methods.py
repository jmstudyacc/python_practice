"""
Methods with Arguments:
-----------------------

Methods can also take more arguments than just self:

class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile
 
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"

Above we defined a DistanceConverter class, instantiated it, and used it to convert 5 miles into kilometers. 
Notice again that even though how_many_kms takes two arguments in its definition, 
we only pass miles, because self is implicitly passed (and refers to the object converter).
"""


class Circle:
    pi = 3.14

    # Since pi is a class variable, you can access it as an attribute of the class
    def area(self, radius):
        return Circle.pi * radius ** 2


circle = Circle()

# the Circle class is instantiated to the circle variable
# when you want to use that class you should call the variable with the method inside it
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)
