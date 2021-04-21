def common_numbers(l1, l2):
    # look up the set methods again...
    result = set(l1).intersection(set(l2))
    print(result)
    return len(result)


lst1 = [5, 3, 3, 10, 40]
lst2 = [40, 3, 40, 1, 2]
print(common_numbers(lst1, lst2))
print("\n")
lst3 = [89, 78, 67, 56, 45, 89, 45]
lst4 = [56, 12, 12, 13, 45, 89]
print(common_numbers(lst3, lst4))
print("\n")
lst5 = [1, 2, 3, 4, 5, 6]
lst6 = [6, 5, 4, 3, 2, 1]
print(common_numbers(lst5, lst6))