"""
Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). 
Print the resulting list. If a list has an odd number of elements, leave the last element in place.

For example, on input:
1 3 2 6 7
output must be
3 1 6 2 7

"""

def adj_numb_swap(nums):
    numSplit = nums.split(" ")          # Split the input into a list based on an empty space
    numLen = len(numSplit)              # Find the length of this new list for the for loop

    if numLen % 2 != 0:                                                 # Testing for ODD length 
        for i in range(0, numLen-1, 2):                                 # We do not want to affect the last value so minus 1 from total range and use 2 as interval
            numSplit[i], numSplit[i+1] = numSplit[i+1], numSplit[i]     # Swap i value with i+1 value
        
        print(numSplit)

    elif numLen % 2 == 0:                                               # Testing for EVEN length
        for i in range(0, numLen, 2):                                   # EVEN length so we can manipulate last value so no change to length
            numSplit[i], numSplit[i+1] = numSplit[i+1], numSplit[i]     # Swap i value with i+1 value
        
        print(numSplit)

    
adj_numb_swap(input())

"""
nums_str = input().split()

for i in range(0, len(nums_str)-1, 2):
  print(nums_str[i+1], nums_str[i], end = " ")              # This version does the FOR loop ONCE and then tests for ODD - should be more efficient
  
if len(nums_str) % 2 == 1:
  print(nums_str[-1])

"""
