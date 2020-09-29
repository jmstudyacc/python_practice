n = int(input("Please enter a value for N: "))

def func_fibonacci(n):  
    if n <= 0:                  # Used to catch a ValueError in the event user does not provide positive number              
        ValueError("Please enter an integer larger than 0")
    elif n == 1:                # First number of FIBONACCI sequence is always 1
        return 1
    elif n == 2:                # Second number of FIBONACCI sequience is always 1
        return 1
    elif n > 2:                 # If input is larger than 2 then Sequence can begin
        return func_fibonacci(n-1) + func_fibonacci(n-2)    # Return the value of F(n-1) + F(n-2)

for i in range(1, n+1):                 # Loop exists OUTSIDE of the function as the LOOP calls the function
    print(i, ": ", func_fibonacci(i))   # You iterate from start to a value and run the FIBONACCI function against that value
                                        # This is why 'i' is used twice in the for loop
func_fibonacci(n)

# This is a bad function as it does not scale well
# The amount of recursion in this function causes it to become painfully slow