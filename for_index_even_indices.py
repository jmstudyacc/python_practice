"""
Read a single line of text containing a list of numbers (separated by space).  Print all the list elements with an even index number. (i.e. A[0], A[2], A[4], ...) 

Hint. Use s.split(), where s is a string, to obtain a list of strings resulting from splitting s using space as separator

For example, on input
13 4 23 4 5 6
output must be
13 23 5

"""
userString = input()
userStringSplit = userString.split(" ")     # split the string based on a 'SPACE'

#print(userStringSplit)

userStringLen = len(userStringSplit)        # Find the length for the for loop

#print(userStringLen)

for i in range(0, userStringLen, 2):        # for loop from 0 to final index incrementing in 2s
    print(userStringSplit[i])
