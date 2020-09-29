# In mathematics, the factorial of an integer n, denoted by n! is the following product:
# n! = 1 × 2 × … × n

# For the given integer n calculate the value 
# 1! + 2! + 3! + ... + n!

# Try to discover the solution that uses only one for-loop. And don't use math module in this exercise.
# Example Input: 4

n = int(input())

f = 1
result = 0

for i in range(1, n+1):
	 f *= i
	 result += f

print(result)