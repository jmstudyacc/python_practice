def recursive_sum(lst):
    # catches the base case
    if len(lst) == 1:
        return lst[0]
    else:
        # return the value of lst[0] + recursive calls - recurse from 1 onwards
        return lst[0] + recursive_sum(lst[1:])


print(recursive_sum([1, 2, 3, 4]))