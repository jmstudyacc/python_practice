
"""
def same_values(lst1, lst2):
    new_lst = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            new_lst.append(i)
    return new_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
"""

def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
        
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
