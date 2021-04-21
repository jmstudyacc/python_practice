def bishop_move(a, b, c, d):
    if abs(a - c) == abs(b - d):
        return "YES"
    else:
        return "NO"


a, b, c, d = [int(input()) for x in range(4)]

print(bishop_move(a, b, c, d))
