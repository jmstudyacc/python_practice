def queen_move(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    else:
        return False


def queens():
    # set default move value to no
    move = "NO"
    # create a list to iterate over
    ql = []
    # iterate 8 times for input and append after splitting
    for i in range(8):
        x = input().split(" ")
        ql.append(x)

    # iterate over the list with outer list to set x1 and y1 values - 1 to improve performance
    for i in range(len(ql) - 1):
        x1 = int(ql[i][0])
        y1 = int(ql[i][1])
        # iterate with inner loop to check the i positions vs j positions
        for j in range(i + 1, len(ql)):     # work from i + 1 as we don't want the code to check i against itself
            x2 = int(ql[j][0])
            y2 = int(ql[j][1])
            # uses queen_move() function, tweaked to return a boolean, to determine if a move is possible
            if queen_move(x1, y1, x2, y2):
                move = "YES"

    return move


print(queens())
