def fib(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        previous_fib_num = fib(n-1)
        previous_previous_fib_num = fib(n-2)
        result = previous_fib_num + previous_previous_fib_num
        return result

print(fib(3))