# File to show import modules and testing exceptions

# Print the square root
# Math library contains the square root function!
# So import it

# if you needed everything from Math library
# from math import *

# If you only want to import the sqrt function
# from math import sqrt
"""
import math  

n = float(input("Please enter a number: "))

result = math.sqrt(n)

print(f"Square Root of {n} is {result}")
"""
# This is great but what happens if an error occurs?
# Or incorrect input is provided?

# If you want to give the code to someone else, e.g. a customer
# You should ensure that you do not have crashes that show debug

# Try...Except is the best way to do this!
"""
import math  

try:
    n = float(input("Please enter a number: "))
    result = math.sqrt(n)
    print(f"Square Root of {n} is {result}")
except:
    print("There was an error!")
"""
# This is better but the error is too vague
# How can we make the error messages more applicable?

"""
import math  

try:
    n = float(input("Please enter a number: "))
    result = math.sqrt(n)
    print(f"Square Root of {n} is {result}")

except Exception as e:                                      # e is a variable here, and captures the information as to what went wrong on this block
    print("There was an error! Here are more details:", e)  # This does not provide specific error messages but gives better direction
"""
# Great! But what about our own functions we define?

# An example here is the factorial function

def my_factorials(n):              # If you want to make a more robust bit of code you should add a check and exception  
    if n < 1:
        raise ValueError("Factorial is defined for positive numbers only.")
    
    product = 1
    
    for i in range(1,n+1):
        product *= i
    
    return product

