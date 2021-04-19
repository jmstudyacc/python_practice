def recursive_max(lst):
    # catches the base case
    if len(lst) == 1:
        return lst[0]
    else:
        # recurse up the list from element 1 onwards
        maxi = recursive_max(lst[1:])
        return maxi if maxi > lst[0] else lst[0]


l1 = [234231, 250, 3, 4]
print(recursive_max(l1))