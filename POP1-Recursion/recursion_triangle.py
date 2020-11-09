
def triangle_print(sideLength):             # Create your function needing sideLength as a var
    if sideLength < 1: return               # If sideLength is less than 1, return nothing

    triangle_print(sideLength - 1)          # Recursively call the function with sideLength minus 1
    print(u"\u25AA" * sideLength)           # Print the UTF-8 value for SMALL BLACK SQUARE multiplied by sideLength value

triangle_print(4)                           # Call the function

# There are 2 key requirements to ensure that recursion is successful
# 1 - Each recursive call must simplify the task in some way
# 2 - There must be special cases to handle the simplest tasks directly
#
# Don't get lost in the complication of the recursive function
