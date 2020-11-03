
# For a given integer N, print all the squares of positive integers 
# where the square is less than or equal to N, in ascending order.

# Example Input: 50

# Example Output: 1 4 9 16 25 36 49

n = int(input())
#...
sq_ints = 1
count = 1

while sq_ints <= n:       # while loop to iterate over numbers to reach 10
	sq_ints = count ** 2    # assign 'sq_ints' to the value of count squared
	if sq_ints <= n:        # if statement to test if sq_ints is less or equal to n
		print(sq_ints)        # print if sq_ints fulfils criteria
	else:         
		break                 # break the loop once finished
	count += 1              # count increments at the end of each loop, like counting up 1, 2, 3
