
# Given three integers, print them in ascending order
# 5
# 3
# 7

list = []

n1 = list.append(int(input()))

n2 = list.append(int(input()))
n3 = list.append(int(input()))

list.sort()

print(list)

"""
a = int(input())
b = int(input())
c = int(input())

if a <= b <= c:
  print(a, b, c, end='\n')
elif a <= c <= b:
  print(a, c, b, end='\n')
elif b <= a <= c:
  print(b, a, c, end='\n')
elif b <= c <= a:
  print(b, c, a, end='\n')
elif c <= a <= b:
  print(c, a, b, end='\n')
else:
  print(c, b, a, end='\n')
  """