def sum_n_numbers():
    # init a value to hold total
    total = 0

    # get the number of loops
    n = int(input())

    # iterate with range of user input
    for i in range(n):
        # add the user input to total
        total += int(input())

    # return total to end function
    return total


print(sum_n_numbers())