xcoord = int(input())
ycoord = int(input())
xcoord2 = int(input())
ycoord2 = int(input())

if xcoord % 2 != 0:
    if ycoord % 2 != 0:
        color = "BLACK"
    else:
        color = "WHITE"

elif xcoord % 2 == 0:
    if ycoord % 2 == 0:
        color = "BLACK"
    else:
        color = "WHITE"

if xcoord2 % 2 != 0:
    if ycoord2 % 2 != 0:
        color2 = "BLACK"
        if color == color2:
          print("YES")
        else:
          print("NO")
    else:
        color2 = "WHITE"
        if color == color2:
          print("YES")
        else:
          print("NO")


elif xcoord2 % 2 == 0:
    if ycoord2 % 2 == 0:
        color2 = "BLACK"
        if color == color2:
          print("YES")
        else:
          print("NO")
    else:
        color2 = "WHITE"
        if color == color2:
          print("YES")
        else:
          print("NO")

"""
x1 = int(input())
y1 = int(input())
1
if (x1 + y1) % 2 == 0:
  print('YES')
else:
  print('NO')
"""