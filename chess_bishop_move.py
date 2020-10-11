
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

"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) == abs(y1 - y2):
  print('YES')
else:
  print('NO')
"""