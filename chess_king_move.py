x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())

if x2 == (x-1) or x2 == (x+1) or x2 == x:
    if y2 == (y-1) or y2 == (y+1) or y2 == y:
        print("YES")
    else:
        print("NO")
else:
    print("NO")