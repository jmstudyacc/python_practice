x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())       # Above gathers coordinate details for the starting point and proposed move

if x2 == (x-1) or x2 == (x+1) or x2 == x:           # x-1 equivalent of moving left, x+1 equivalent of moving right
    if y2 == (y-1) or y2 == (y+1) or y2 == y:       # y-1 equivalent of moving down, y+1 equivalent of moving up
        print("YES")
    else:
        print("NO")
else:
    print("NO")