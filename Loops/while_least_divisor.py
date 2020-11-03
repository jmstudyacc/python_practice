
# Given an integer not less than 2. 
# Print its smallest integer divisor greater than 1.

# Example Input: 15

# Example Output: 3

n = int(input())  #

if n >= 2:                      # Test to check if n is larger than 2
  for i in range(1, n + 1):     # for loop iterating from 1 and going to n + 1, as it would stop before n
    if n % i == 0 and i > 1:    # if n modulo i returns 0 (no remainder) and value of i is greater than 1
      div = i                   # assign div variable to value of i - this will always be more than 1 due to above
      print(div)                # print the value associated with div
      break                     # least integer has been found so break the loop

"""
n = int(input())				

i = 2

finished = False

while not finished:				# use boolean logic to keep the loop going
  if n % i == 0:				# if n modulo i provides is 0 
    finished = True				# Change the finished boolean to True
  else:							
    i+=1						# Else, add 1 to i and continue the loop

print(i)
"""
