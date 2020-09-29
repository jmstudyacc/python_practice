
"""
aint = int(input())
bint = int(input())

for i in range(aint, (bint+1), 1):
	print(i, end=' ')   # This places a space ' ' at the end of each output

"""

aint = int(input())
bint = int(input())

if aint < bint:
	for i in range(aint, bint+1, 1):
		print(i, end=' ')
else:
	for i in range(aint, bint-1, -1):
		print(i)