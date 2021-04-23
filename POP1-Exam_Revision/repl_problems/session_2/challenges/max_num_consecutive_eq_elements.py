def widest_fragment():
    # var to hold the current maximum width
    maxi = 0

    # var to hold the temporary width size
    w_size = 1

    # var to hold the previous user input for comparison with next user input
    temp_int = 0
    while True:
        n = int(input())

        # case to break out of the loop
        if n == 0:
            break

        # if n equals previous input
        if n == temp_int:
            # increase width size by 1 e.g. becomes 2
            w_size += 1
            # store the value of w_size in maxi if it is bigger than last stored maxi value
            if w_size > maxi:
                maxi = w_size
        # reset w_size back to 1
        else:
            w_size = 1

        # store user input n in temp_int ahead of next iteration
        temp_int = n

    return maxi


print(widest_fragment())


