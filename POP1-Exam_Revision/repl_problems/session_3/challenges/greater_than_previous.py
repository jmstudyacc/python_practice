def greater_than_previous(ln):
    # hold successful values in gtp_nums list
    gtp_nums = []
    for i in range(1, len(ln)):
        # if value at i in ln is bigger than i-1 in ln
        if ln[i] > ln[i-1]:
            # append the value to a new list and convert to a string when you do
            gtp_nums.append(str(ln[i]))

    # join the string list into a string sep by a space
    return " ".join(gtp_nums)


l1 = [10, 6, 11, 13, 10, 10, 23]
l2 = [5, 10, 15, 20, 25, 30, 35]
l3 = [5, 4, 5, 5, 5, 6, 7, 5, 6, 7]
print(greater_than_previous(l1))
print(greater_than_previous(l2))
print(greater_than_previous(l3))
