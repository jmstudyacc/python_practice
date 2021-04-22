def ladder(n):
    # outer loop to enable the prints by j
    for i in range(1, n+1):
        # j starts at 1 so 1 is placed first on each row
        # j's range is 1 more than i to enable the inclusive printing
        # on i = 1 j can iterate up to i+1 which enables row 3 to print up to 3
        for j in range(1, i+1):
            print(j, end="")
        print("")


ladder(3)
ladder(5)
ladder(9)