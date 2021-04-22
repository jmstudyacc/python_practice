def sum_factorial(n):
    # 1 variable to hold the factorial
    FAC = 1

    # one to hold the total
    TOTAL = 1

    # factorial of 1 is 1 so begin fac/total at 1 and increment
    for i in range(1, n):
        # calculate the factorial in the loop
        FAC += FAC * i

        # add the factorial to total
        TOTAL += FAC

    return n, TOTAL


print(sum_factorial(3))
print(sum_factorial(4))
print(sum_factorial(5))
