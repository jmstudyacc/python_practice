"""
Self:
-----
Since we can already use dictionaries to store key-value pairs, using objects for that purpose is not really useful. 
Instance variables are more powerful when you can guarantee a rigidity to the data the object is holding.

This convenience is most apparent when the constructor creates the instance variables, using the arguments passed in to it. 
If we were creating a search engine, and we wanted to create classes for each separate entry we could return. We’d do that like this:

class SearchEngineEntry:
  def __init__(self, url):
    self.url = url
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.url)
# prints "www.codecademy.com"
 
print(wikipedia.url)
# prints "www.wikipedia.org"

Since the self keyword refers to the object and not the class being called, 
we can define a secure method on the SearchEngineEntry class that returns the secure link to an entry.

class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url
 
  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.secure())
# prints "https://www.codecademy.com"
 
print(wikipedia.secure())
# prints "https://www.wikipedia.org"

Above we define our secure() method to take just the one required argument, self. 
We access both the class variable self.secure_prefix and the instance variable self.url to return a secure URL.

This is the strength of writing object-oriented programs. 
We can write our classes to structure the data that we need and write methods that will interact with that data in a meaningful way.
"""
# In Circle‘s constructor set the instance variable self.radius to equal half the diameter that gets passed in.


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2

    def circumference(self):
        # Note that you have to call 'self.' before using a variable e.g. pi and radius
        circumference = 2 * self.pi * self.radius
        return circumference


# Define three Circles with three different diameters.
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# Call the 'circumference' method from the Circle class with 'Circle.circumference'
print(Circle.circumference(medium_pizza))
print(Circle.circumference(teaching_table))
print(Circle.circumference(round_room))
