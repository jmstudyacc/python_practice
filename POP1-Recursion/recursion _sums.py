"""
Implement a function my_sum(lst) that given a list lst of interger numbers, returns the sum of them.

In this exercise, do not use the standard sum function and no loop of any kind. Implement the function recursively using the following idea:

- If the list contains one element, the sum of the list is equal to this element
- If the list contains more elements, the sum of the list is equal to the first element plus the sum of the remaining list

For example, on input:
print(my_sum([1,2,3]))

Output must be:

6
""" 

def my_sum(lst):
    if (len(lst)) == 1:
        return lst[0]
    
    else:
        return lst[0]+ my_sum(lst[1:])          # return index of lst at pos 0 = 3, + value of my_sum(index of lst at pos 1 -->)
    
a = [3,3,3,4]

print(my_sum(a))


"""
def my_sum(lst):
  if len(lst)==1:
    return lst[0]
  
  else:
    
    rest_sum = my_sum(lst[1:])
    return lst[0]+rest_sum
    
"""