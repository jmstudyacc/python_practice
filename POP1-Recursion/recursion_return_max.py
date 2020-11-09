"""
Implement a function my_max(lst) that given a list of integer numbers lst returns its maximum.

Do not use the standard function max or a loop of any kind. Instead implement my_max recursively relying on the following principle:

- if list contains just one element n then its maximum is equal n
- othewise,  the maximum is either the first value in the list or the maximum of the rest of the list, whichever is larger 

For example, the result of
print(my_max([3,2,5]))
must be
5
"""
def my_max(lst):
    if len(lst) == 1:           # Base case, if length of the list var equals 1
        return lst[0]           # Return the value of the list
    
    else:
        a = my_max(lst[1:])     # If not Base Case, call the function AFTER lst[0] for values lst[1:]

        if a > lst[0]:          # IF a is greater than value currently at lst[0]
            return a            
        else:                   # ELSE return the value of lst[0]
            return lst[0]
                                # a now becomes the returned value of this ELSE statement e.g. lst[0] = '5'

print(my_max([3, 2, 5]))

"""

def my_max(lst):
    a = 0
    b = len(lst)
    
    if b == 1:
        return lst[0]

    else:
        return sorted(lst)[-1] 

l = [3, 2, 5]

print(my_max(l))
"""   

"""
MODEL SOLUTION:

def my_max(lst):
  if len(lst)==1:
    return lst[0]
  
  else:
    tail_max = my_max(lst[1:])
    
    if tail_max > lst[0]:
      return tail_max
    
    else:
      return lst[0]

"""