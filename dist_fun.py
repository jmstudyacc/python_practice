N = int(input())
M = int(input())

distance = 0
counter = 0

while distance < M:
  distance += N
  counter += 1

print(counter)

"""
from math import ceil

n = int(input())
m = int(input())
print(ceil(m / n))
"""