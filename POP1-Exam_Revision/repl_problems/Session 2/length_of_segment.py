import math


# distance between (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):

    # (x1 - x2)^2 + (y1 - y2)^2
    length = pow((x1 - x2), 2) + pow((y1 - y2), 2)

    # sqrt the answer which also eliminates negatives
    # √(length)
    length = math.sqrt(length)
    return length


a, b, c, d = [int(input()) for x in range(4)]
print(distance(a, b, c, d))
