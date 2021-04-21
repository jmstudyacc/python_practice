"""
Suppose f is a function that takes a character (string of length 1) as an argument and returns a character. Define a higher order function stringify that takes f as an argument and returns another function F such that:
F takes a string s as an argument
F returns a string which is equal to f(s[0])f(s[1])...f(s[n])

Use the pattern on the right for your implementation.

Hint: Have a look at the function vectorize in the lecture slides.

For example, the result of:
def f(x):
    #change lower case to upper
    return chr(ord(x)-32)
F = stringify(f)
print(F("apple"))

Must be:
APPLE

def f(x):
    #change lower case to upper
    return chr(ord(x)-32)
F = stringify(f)
#Test1 checks F("apple")=="APPLE"

def f(x):
    #change upper case to lower
    return chr(ord(x)+32)
F = stringify(f)
#Test2 checks F("APPLE")=="apple"

def f(x):
    #change lower case to upper if vowel
    #otherwise leave unchanged
    if x in {'a', 'e', 'i', 'o', 'u'}:
        return chr(ord(x)-32)
    else:
        return x

F = stringify(f)

#Test3 checks F("apple") == "ApplE"
"""


# code starts by loading both f(x) and stringify(f) as objects
def f(x):
    # change lower case to upper
    return chr(ord(x) - 32)     # x referenced in this function is the value passed by the loop below
    # the letter returned after running this function is the capitalised version of the original letter input


# runs stringify(f) function and value
def stringify(f):
    # loads new_string() function with 's' as value - function: new_string(s) parent: stringify(f)
    def new_string(s):
        # like setting a counter to 0 and then iterating, this sets the string var to empty which will be added to
        string = ""
        # looping with x over the value in the variable s (see below for value)
        for x in s:
            # add the result of function f() against iterated value 'x'
            string += f(x)  # x is then run against f(x) which is a function to capitalise the letter

        # the string variable will contain the capitalised version of 'x' and continue to loop until at end of 's'
        return string
        # when loop is completed the new_string() function returns the value of 'string'

    return new_string


# F is assigned to the value of the function stringify(f) calling the f(x)
F = stringify(f)
# calling the function stringify(f) with a string value of "apple" - this maps to the value needed in new_string(s)
print(F("apple"))
