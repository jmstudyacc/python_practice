"""
Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such pair, leave the output blank. 

For example, on input
-1 2 -3 -4 -5 1 2
output must be
-3 -4

"""

userString = input()

userStringSplit = userString.split(" ")     # split the string based on a 'SPACE'

userStringLen = len(userStringSplit)        # Find the length for the for loop

userStringToInt = []                        # Create an empty list

for i in range(0, userStringLen,1):         # Iterate over the list that is a string and append to a new list for Integers
    userValue = userStringSplit[i]
    userStringToInt.append(int(userValue))  # Append to the empty list for integers

for i in range(0, userStringLen, 1):        # Iterate over the new list 
    if i+1 >= userStringLen:                # If i+1 is larger than the list then break as this will cause an error 
        break
    else:                                   
        if userStringToInt[i] < 0 and userStringToInt[i+1] < 0:         # If both of the index value are less than 0 - ergo negative
            print(userStringToInt[i], userStringToInt[i+1])             # Print the two values and break the loop
            break

        elif userStringToInt[i] >= 0 and userStringToInt[i+1] >= 0:     # If the two values are larger than or equal to 0 - ergo positive
            print(userStringToInt[i], userStringToInt[i+1])             # Print the result
            break