"""
Instance Variables:
-------------------

We’ve learned so far that a class is a schematic for a data type and an object is an instance of a class, 
but why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has? 
This is because each instance of a class can hold different kinds of data.

The data held by an object is referred to as an instance variable. 
Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.

Let’s say that we have the following class definition:

class FakeDict:
  pass

We can instantiate two different objects from this class, fake_dict1 and fake_dict2, 
and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
 
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
 
# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"

"""


class Store:
    pass


# Create two objects from this store class, named alternative_rocks and isabelles_ices.
alternative_rocks = Store()
isabelles_ices = Store()

# Give them both instance attributes called store_name. Set alternative_rocks‘s store_name to "Alternative Rocks".
# Set isabelles_ices‘s store_name to "Isabelle's Ices".
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"
