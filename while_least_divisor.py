
# Given an integer not less than 2. 
# Print its smallest integer divisor greater than 1.

# Example Input: 15

# Example Output: 3

n = int(input())

if n >= 2:
	for i in range(1, n + 1):
		if n % i == 0 and i > 1:
			div = i
			print(div)
			break                       # Break statement kills the loop so it only prints the smallest above 1