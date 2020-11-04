"""
Implement a function expo(a,n) that computes the result of a**n (a to the power of n) for a number a and non-negative integer n. 

Do not use ** operation itself and any kind of loop in this exercise. 

Instead, make the function expo recursive relying on the following principle:

- a**0 = 1
- a**n = a * (a**(n-1))

For example, result of print(expo(2,3))

Must be:

8
"""
def expo(a,n):
  if n < 0:
    return ValueError("Please enter an integer larger than 0")
    
  elif n == 0:                          # Capture the 0 input for the non-recursive branch/base case
    return 1
  
  else:
    return a*(expo(a, n-1))           # Returns A multiply result of function
    
print(expo(2,3))