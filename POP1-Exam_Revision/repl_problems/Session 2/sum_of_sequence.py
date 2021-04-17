def sum_of_sequence():
    dog = True
    total = 0

    # while loop as it is unknown how many input
    while dog:
        # try/except because empty input causes crash
        try:
            a = int(input())
            if a == 0:
                dog = False
            else:
                total += a
        # except to catch a ValueError
        except ValueError:
            continue

    return total


print(sum_of_sequence())
