def factorial(n):
    if n == 1:
        return 1
    else:
        # multiply n by recursive call to n-1
        total = n * factorial(n-1)
        return total


a = 4
print(factorial(a))