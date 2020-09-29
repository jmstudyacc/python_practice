
# For a given integer N, print all the squares of positive integers 
# where the square is less than or equal to N, in ascending order.

# Example Input: 50

# Example Output: 1 4 9 16 25 36 49

n = int(input())
sq_ints = 1
count = 1

while sq_ints <= n:
	sq_ints = count ** 2
	if sq_ints <= n:
		print(sq_ints)
	else:
		break
	count += 1