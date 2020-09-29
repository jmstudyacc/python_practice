# There was a set of cards with numbers from 1 to N. One of the card is now lost. 
# Determine the number on that lost card given the numbers for the remaining cards.

# Given a number N, followed by N − 1 integers representing the numbers on the remaining cards (distinct integers in the range from 1 to N). 
# Find and print the number on the lost card.

# Example Input: 5 3 5 2 1
"""
n = int(input())

total1 = 0
total2 = 0

for i in range(1, n+1):
	total1 += i
	
for j in range(n-1):
	total2 += int(input())
	
print(total1 - total2)

# Mathematically here the easiest answer is to add up all the numbers
# Add all the numbers in the input and then subtract from the original total
"""

    
# For given integer n ≤ 9 print a ladder of n steps. 
# The k-th step consists of the integers from 1 to k without spaces between them.
# To do that, you can use the sep and end arguments for the function print().

k = int(input())
nstring = ''

for i in range(1, k+1):
    n = str(i)
    nstring += n
    print(nstring)