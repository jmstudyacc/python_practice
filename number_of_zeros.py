# Given N numbers: the first number in the input is N, after that N integers are given. 
# Count the number of zeros among the given integers and print it.
# You need to count the number of numbers that are equal to zero, not the number of zero digits.

# Example Input: 5 0 700 0 200 2

n = int(input())
zeros = 0

for i in range(n):
	n2 = int(input())
	if n2 == 0:
		zeros+= 1
		
		
print(zeros)
		