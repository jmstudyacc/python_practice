# N students take K pens - 2 variables
# distribute/divide - among each other evenly
# Remainder should stay in the box - floor division

n = int(input())
k = int(input())

sharedPencils = k // n
pencilsInBox = k - (sharedPencils*n)

print(sharedPencils)
print(pencilsInBox)