# Given three integers. Determine how many of them are equal to each other. The program must print one of the numbers: 
# 3 (if all are same) 
# 2 (if two of them are equal to each other and the third one is different) 
# 0 (if all numbers are different).

# Example Inputs:
# 10 5 10

# Example Outputs:
# 2

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 != num2 and num1 != num3:
	print(1)
elif num2 != num3 and num2 != num1:
	print(2)
else:
	print(3)