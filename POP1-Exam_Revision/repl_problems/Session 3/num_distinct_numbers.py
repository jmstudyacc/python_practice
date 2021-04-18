def distinct_nums(L):
    s1 = set(L)
    return len(s1)


l1 = [5, 3, 2, 3, 2, 4]
l2 = [10, 10, 10, 10, 10]
l3 = [1, 10, 10, 1, 10, 20]
l4 = [5, 4, 3, 2, 1]
print(distinct_nums(l1))
print(distinct_nums(l2))
print(distinct_nums(l3))
print(distinct_nums(l4))