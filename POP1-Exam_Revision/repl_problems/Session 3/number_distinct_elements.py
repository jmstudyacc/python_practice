def num_distinct_elements(lst):
    elements = set(lst)
    return len(elements)


Lst = [1, 1, 2, 3, 3]
print(num_distinct_elements(Lst))
print("\n")
Lst = [2, 3, 4, 5]
print(num_distinct_elements(Lst))
print("\n")
Lst = [10, 20, 20, 30, 30, 40, 40, 40, 50, 60, 60]
print(num_distinct_elements(Lst))


