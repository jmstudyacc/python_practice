# if the input is a number in the fibonacci sequence return its index
def index_fibo(n):
    # n1 holds 0 (1st), n1 holds 1 (2nd)
    n1, n2 = 0, 1
    # index value
    i = 0
    # result of fib sequence
    fib = 0

    # if n is 0 return index 1
    if n == n1:
        return 1

    # if n is 1 return index 2
    if n == n2:
        return 2

    # while loop to calculate fibonacci series - if the result of the fib sequence is greater than n terminate loop
    while fib < n:
        # nth term is n1 + n2
        nth = n1 + n2
        # fibonacci number is the result of n2
        fib = n2
        # shift values around for fibo calc
        n1 = n2
        # n2 equals the result of adding n1 & n2 together
        n2 = nth
        # increase index count at end of each loop
        i += 1

    # if the fibonacci answer is larger than the input then n is not in fibonacci series
    if fib > n:
        return -1
    # otherwise fib must equal n at some iteration and the index should be returned
    else:
        return i


print(index_fibo(10))
print(index_fibo(2))
print(index_fibo(8))
print(index_fibo(55))