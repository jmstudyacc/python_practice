def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def fib_nums(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_nums(n - 1) + fib_nums(n - 2)


print("Fibonacci Sequence:")
for i in range(1):
    print(f"{i}: {fib_nums(i)}")

#answer = fib_nums(int(input()))
#print(answer)
