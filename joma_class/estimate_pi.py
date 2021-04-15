# estimate pi when given a range for random number generation
# joma tech - pvimAM_SLic

import random

def estimate_pi(n):
    # initialising the variables that will hold the points
    num_point_circle = 0
    num_point_total = 0

    # iterate an amount equal to n - this is the generation of the point, 1 loop = 1 point
    for _ in range(n):
        # the below code calls the random module, the uniform function and generates a number range 0 -> 1 e.g. 0.1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # mathematical formula to find the distance of a point from the origin (often a square root included)
        distance = x ** 2 + y ** 2

        # if the result is smaller than 1 then it is within the circle
        if distance <= 1:
            num_point_circle += 1

        # if not it is in the square but not the circle
        num_point_total += 1

    # see the formula to understand the isolation of pi
    return 4 * num_point_circle / num_point_total


print(estimate_pi(int(input("Number of points: \n"))))
