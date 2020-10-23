"""
Implement a function numb_of_distinct(L) that given a list L of numbers with all of its elements in ascending order, 
returns the quantity of distinct elements in it.

For example, the result of:

Lst = [1,1,2,3,3]

print(numb_of_distinct(Lst))

Must be:

3
"""

Lst = [1,1,2,3,3,5,6,7,8,9,9]

def distinct_num(Lst):
    LstSet = list(set(Lst))            # Sets have to contain unique values only
    return len(LstSet)                 # Return the length of the Set which should be the total unique values 

print(distinct_num(input()))


"""
def numb_of_distinct(L):
  cnt = 1                           # count var set to 1
  for i in range(0, len(L)-1):      # iterate over list with a range of len -1
    if L[i] != L[i+1]:              # Check if iteration does not equal iteration+1
      cnt+=1                        # If it does increment count to show how many are unique
  return cnt
  
print(numb_of_distinct([1,1,2,3,3,5,6,7,8,9,9]))

"""