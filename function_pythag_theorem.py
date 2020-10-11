import math

# a² + b² = c²
# √(a² + b²) = c

def distance(x1, y1, x2, y2):
    xdiff = abs(x1 - x2)                # Find the difference between 2 X coordinates to get side 1 - use abs to avoid negative numbers although this is not needed due to squaring
    ydiff = abs(y1 - y2)                # Find the difference between 2 Y coordinates to get side 2

    z = (xdiff ** 2) + (ydiff ** 2)     # Assign value of a² + b² to arbitary var 

    hypo = math.sqrt(z)                 # Find answer by getting square root of previous var

    return hypo


d = distance(1,2,6,8)
print(d)