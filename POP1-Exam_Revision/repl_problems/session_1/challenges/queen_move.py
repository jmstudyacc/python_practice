def queen_move(x1, y1, x2, y2):
    # if the x values are the same or the y values are the same - queen is moving like rook
    # if the diff between x values equals the diff between y values - queen is moving like bishop
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return "YES"
    else:
        return "NO"


print(queen_move(4, 2, 6, 3))
print(queen_move(4, 2, 7, 5))
print(queen_move(4, 2, 4, 8))
print(queen_move(5, 3, 6, 5))
print(queen_move(5, 3, 5, 4))