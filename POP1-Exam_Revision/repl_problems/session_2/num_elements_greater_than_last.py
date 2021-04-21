def num_elements_greater_than_last():
    dog = True

    # make a list to hold the values
    list1 = []

    # total variable to increment as needed
    total = 0

    while dog:
        a = int(input())
        # catches the quit case
        if a == 0:
            break
        # appends the input value to the list
        else:
            list1.append(a)

    # check over the list for list at index compared to list at index+1 - if it index+1 is bigger increase total by 1
    for i in range(len(list1) - 1):
        if list1[i] < list1[i+1]:
            total += 1

    return total


print(num_elements_greater_than_last())
