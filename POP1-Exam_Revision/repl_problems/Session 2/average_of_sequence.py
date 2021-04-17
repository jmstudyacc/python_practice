def average_of_sequence():
    dog = True
    total = 0
    loops = 0

    # while loop as it is unknown how many input
    while dog:
        # try/except because empty input causes crash
        try:
            a = int(input())
            if a == 0:
                loops -= 1
                dog = False
            else:
                total += a
        # except to catch a ValueError
        except ValueError:
            print("Error, input value again")
            continue

        loops += 1

    return total // loops


print(average_of_sequence())
