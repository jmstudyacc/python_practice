xcoord = int(input())
ycoord = int(input())

if xcoord % 2 != 0:
    if ycoord % 2 != 0:
        color = "BLACK"
        #print(color)
    else:
        color = "WHITE"
        #print(color)

elif xcoord % 2 == 0:
    if ycoord % 2 == 0:
        color = "BLACK"
        #print(color)
    else:
        color = "WHITE"
        #print(color)

xcoord2 = int(input())
ycoord2 = int(input())

if xcoord2 % 2 != 0:
    if ycoord2 % 2 != 0:
        color2 = "BLACK"
        #print(color2)
    else:
        color2 = "WHITE"
        #print(color2)

elif xcoord2 % 2 == 0:
    if ycoord2 % 2 == 0:
        color2 = "BLACK"
        #print(color2)
    else:
        color2 = "WHITE"
        #print(color2)

if color == color2:
    print("YES")
else:
    print("NO")
