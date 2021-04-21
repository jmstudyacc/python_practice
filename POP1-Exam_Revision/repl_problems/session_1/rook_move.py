def rook_move(a, b, c, d):
    if a == c or b == d:
        return "YES"
    else:
        return "NO"


a, b, c, d, = [int(input()) for x in range(4)]
print(rook_move(a, b, c, d))
