def fib(n):     # Writes Fibonacci sequence up to n
    a, b = 0, 1

    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    
    print()

def fib2(n):     # Returns Fibonacci sequence up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    
    return result

if __name__ == "__main__":      # Include this in the code to make it into a script
    import sys                  # It does not change its ability to be called as a module
    fib(int(sys.argv[1]))       # If the module is imported the code is not run