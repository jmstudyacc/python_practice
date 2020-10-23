
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:                # If X or Y coord has not changed this means the Queen is moving vertically or horizontally
    print("YES")                        # Horizontal or Vertical moves of any length are legal

elif abs(x1 - x2) == abs(y1 - y2):      # If X1 minus X2 is the same as Y1 minus Y2 (when ignoring negatives)
    print("YES")                        # that means the Queen moves in a diagonal left/right/up/down - a legal move

else:                                   # Anything else would be illegal
    print("NO")




x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())

xy = x + y
xy2 = x2 + y2
xy3 = x + y
xy4 = x2 + y2

if xy == xy2:
    print("YES")
elif xy3 % 2 == 0 and xy4 % 2 == 0:
    print("YES")
elif xy3 % 3 == 0 and xy4 % 3 == 0:
    print("YES")
else:
    print("NO")