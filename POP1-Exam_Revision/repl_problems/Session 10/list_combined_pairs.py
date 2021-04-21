
Xstrs = input().split()
X = [int(i) for i in Xstrs]

Ystrs = input().split()
Y = [int(i) for i in Ystrs]

# Z will be a list of tuples that are values in X and Y ONLY if x is smaller than the proposed y value
Z = [(x, y) for x in X for y in Y if x < y]


for pair in Z:
    print(pair[0], pair[1])
