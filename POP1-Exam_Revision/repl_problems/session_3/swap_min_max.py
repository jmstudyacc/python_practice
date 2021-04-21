def swap_min_max(lst):
    # in-built python method to get the index of an element
    mini = lst.index(min(lst))

    # here the process gets the maximum of the list AND gets the index of that element
    maxi = lst.index(max(lst))

    lst[mini], lst[maxi] = lst[maxi], lst[mini]
    return lst


lst = [5, 7, 3, 2, 1, 6]
print(lst)
print(swap_min_max(lst))
print("\n")
lst = [10, 15, 20, 25, 30]
print(lst)
print(swap_min_max(lst))
print("\n")
lst = [76, 45, 47, 80, 85, 50, 55]
print(lst)
print(swap_min_max(lst))