
def fun(n):
    if n < 10: return n
    else: return fun( n // 10) + n % 10


print(fun(19))

# this function returns a value that is the sum of the digits in the number