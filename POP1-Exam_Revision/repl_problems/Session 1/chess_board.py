def chess_board(c1, r1, c2, r2):
    if (c1 + r1 + c2 + r2) % 2 == 0:
        return "YES"
    else:
        return "NO"


a, b, c, d = [int(input()) for x in range(4)]
print(chess_board(a, b, c, d))
