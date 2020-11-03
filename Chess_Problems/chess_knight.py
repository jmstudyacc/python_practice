

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) == 1 and abs(y1 - y2) == 2:     # If the x coordinate has incremented/decremented by 1 and y incr/decr by 2 
    print("YES")                                # the move is legal

elif abs(x1 - x2) == 2 and abs(y1 - y2) == 1:   # Alternative way round, if x coord has incr/decr by 2 and y incr/decr by 1
    print("YES")                                # the move is legal

else:                                           # Anything else is an illegal move
    print("NO")
