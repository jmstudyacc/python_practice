def swap_adj(lst):
    length = len(lst)
    if length % 2 != 0:
        for i in range(0, length-2, 2):
            lst[i], lst[i+1] = lst[i+1], lst[i]
    else:
        for i in range(0, length - 1, 2):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return lst


l = [1, 3, 2, 6, 7]
print(swap_adj(l))
print("\n")
l = [34, 45, 56, 12, 34, 4]
print(swap_adj(l))
print("\n")
l = [1, 1, 3, 3, 5, 5, 6]
print(swap_adj(l))