def king_move(x1, y1, x2, y2):
    # a king can 1 space in any direction therefore x or y needs to equal abs(1)
    if abs(x1 - x2) == 1 or abs(y1 - y2) == 1:
        return "YES"

    return "NO"


print(king_move(3, 4, 4, 5))
print(king_move(2, 3, 1, 4))
print(king_move(5, 7, 4, 6))
print(king_move(5, 6, 4, 7))
print(king_move(1, 1, 1, 3))
print(king_move(8, 8, 2, 4))
print(king_move(5, 6, 3, 6))


