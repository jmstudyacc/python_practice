def maximum_of_sequence():
    dog = True

    # changed to list to sort
    list1 = []

    # while loop as it is unknown how many input
    while dog:
        # try/except because empty input causes crash
        try:
            a = int(input())
            if a == 0:
                dog = False
            else:
                # changes to get max of inputs, so append each value to the list and sort
                list1.append(a)
                list1.sort()
        # except to catch a ValueError
        except ValueError:
            continue

    return list1[-1]


print(maximum_of_sequence())