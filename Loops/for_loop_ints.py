# 10 numbers are given in the input. Read them and print their sum. 
# Use as few variables as you can.

# Example Input: 0 1 2 3 4 5 6 7 8 9

t = 0
for i in range(0, 10, 1):
	n = int(input())
	t += n
print(t)


# N numbers are given in the input. Read them and print their sum.
# The first line of input contains the integer N, which is the number of integers to follow. 
# Each of the next N lines contains one integer. Print the sum of these N integers.

# Example Input: 10 | 1 2 1 1 1 1 3 1 1 1

n = int(input())

t = 0

for i in range(n):
	u = int(input())
	t += u
	
print(t)

# For the given integer N calculate the following sum:
# 1³ + 2³ + ... + N³

n = int(input())
t = 0

for i in range(1, n+1):
	a = i ** 3
	t += a
	
print(t)
