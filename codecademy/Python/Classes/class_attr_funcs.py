"""
Instance variables and class variables are both accessed similarly in Python. 
This is no mistake, they are both considered attributes of an object. 
If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.

class NoCustomAttributes:
  pass
 
attributeless = NoCustomAttributes()
 
try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")
 
# prints "This text gets printed!"

What if we aren’t sure if an object has an attribute or not? 
hasattr() will return True if an object has a given attribute and False otherwise. 
If we want to get the actual value of the attribute, getattr() is a Python function that will return the value of a given object and attribute. 
In this function, we can also supply a third argument that will be the default if the object does not have the given attribute.

The syntax and parameters for these functions look like this:

hasattr(object, “attribute”) has two parameters:

    object : the object we are testing to see if it has a certain attribute
    attribute : name of attribute we want to see if it exists

getattr(object, “attribute”, default) has three parameters (one of which is optional):

    object : the object whose attribute we want to evaluate
    attribute : name of attribute we want to evaluate
    default : the value that is returned if the attribute does not exist (note: this parameter is optional)

Calling those functions looks like this:

hasattr(attributeless, "fake_attribute")
# returns False
 
getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

Above we checked if the attributeless object has the attribute fake_attribute. 
Since it does not, hasattr() returned False. After that, we used getattr to attempt to retrieve other_fake_attribute. 
Since other_fake_attribute isn’t a real attribute on attributeless, our call to getattr() returned the supplied default value 800, 
instead of throwing an AttributeError.
"""
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

# For every element in the list, check if the element has the attribute count using the hasattr() function.
# If so, print the following line of code:
for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
    # Now let’s add an else statement for the elements that do not have the attribute count. In this else statement add the following line of code:
    else:
        print(str(type(element)) + " does not have the count attribute :(")
