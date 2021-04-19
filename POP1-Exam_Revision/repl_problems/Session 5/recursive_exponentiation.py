def memoize(f):
    # creates a dictionary to store values
    memo = {}

    # helper function for memoization
    # you have to pass it the same variables as your target function
    def helper(x, y):
        # if it is not present, create an entry in dictionary
        if x not in memo:
            # this entry is the result of calling the function on the target variables
            memo[x] = f(x, y)

        # return the result of memo[x] to the memoize function
        return memo[x]

    # returns the result of the helper function
    return helper


@memoize
def expo(a, n):
    # if n is equal to 0, return 1
    if n == 0:
        return 1
    else:
        # variable to hold the result of recursive function call to n - 1
        expo_n_minus_1 = expo(a, n-1)

        # returns the variable multiplied by a
        return expo_n_minus_1 * a

    # that will recurse until n = 0 and then operations begin


print(f"Recursive exponent operator: {expo(1024, 2)}")
print(f"Normal exponent operator: {1024 ** 2}")
