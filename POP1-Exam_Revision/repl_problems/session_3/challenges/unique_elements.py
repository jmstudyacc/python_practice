def unique_elements(lst):
    [print(lst[x], end=" ") for x in range(len(lst)) if lst.count(lst[x]) == 1]


l1 = [4, 5, 20, 4, 5, 10]
l2 = [10, 10, 10, 20, 20, 1, 10, 5, 9, 9, 7]
l3 = [1, 2, 3, 4, 5, 6]
unique_elements(l1)
print("\n")
unique_elements(l2)
print("\n")
unique_elements(l3)
