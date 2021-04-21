# creates lists from user input and converts the input into an int as well as a list
X = [int(x) for x in input().split()]
Y = [int(y) for y in input().split()]

# zips the 2 lists, but first squares 'x' value in list 'X' & uses that to zip with Y
squared_map = zip((x ** 2 for x in X), Y)

for x in squared_map:
    print(x[0], x[1])

