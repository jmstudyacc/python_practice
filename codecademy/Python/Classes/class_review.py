"""
Review

So far we’ve covered what a data type actually is in Python. 
We explored what the functionality of Python’s built-in types (also referred to as primitives) are. 
We learned how to create our own data types using the class keyword.

We explored the relationship between a class and an object — we create objects when we instantiate a class, 
we find the class when we check the type() of an object. We learned the difference between class variables (the same for all objects of a class) 
and instance variables (unique for each object).

We learned about how to define an object’s functionality with methods. We created multiple objects from the same class, 
all with similar functionality, but with different internal data. They all had the same methods, 
but produced different output because they were different instances.

Take a moment to congratulate yourself, object-oriented programming is a complicated concept.
"""

# Define a class Student this will be our data model at Jan van Eyck High School and Conservatory.


class Student():

    # Add a constructor for Student. Have the constructor take in two parameters:
    # a name and a year. Save those two as attributes .name and .year.
    def __init__(self, name, year):
        self.name = name
        self.year = year
    # In the body of the constructor for Student, declare self.grades as an empty list.
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)

# Create a Grade class, with minimum_passing as an attribute set to 65


class Grade():
    minimum_passing = 65
    # Give Grade a constructor. Take in a parameter score and assign it to self.score.

    def __init__(self, score):
        self.score = score

    def is_passing(self, score):
        self.score = score
        if self.score >= self.minimum_passing:
            return True


# Create three instances of the Student class:

#    Roger van der Weyden, year 10
#    Sandro Botticelli, year 12
#    Pieter Bruegel the Elder, year 8

# Save them into the variables roger, sandro, and pieter.


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))

pieter.is_passing()
