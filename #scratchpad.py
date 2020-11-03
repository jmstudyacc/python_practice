"""
months = ("0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")

month = int(input("What month do you pick? "))
day = int(input("Which day do you pick? "))


if month == 1 and day != 31: 
    print(months[month], day+1)
elif month == 1 and day == 31:
    print(months[month+1], "1")

elif month == 2 and day != 28:
    print(months[month], day+1)
elif month == 2 and day == 28:
    print(months[month+1], "1")

elif month == 3 and day != 31: 
    print(months[month], day+1)
elif month == 3 and day == 31:
    print(months[month+1], "1")

elif month == 4 and day != 30:
    print(months[month], day+1)
elif month == 4 and day == 30:
    print(months[month+1], "1")

elif month == 5 and day != 31: 
    print(months[month], day+1)
elif month == 5 and day == 31:
    print(months[month+1], "1")

elif month == 6 and day != 30:
    print(months[month], day+1)
elif month == 6 and day == 30:
    print(months[month+1], "1")

elif month == 7 and day != 31: 
    print(months[month], day+1)
elif month == 7 and day == 31:
    print(months[month+1], "1")

elif month == 8 and day != 31:
    print(months[month], day+1)
elif month == 8 and day == 31:
    print(months[month+1], "1")

elif month == 9 and day != 30: 
    print(months[month], day+1)
elif month == 9 and day == 30:
    print(months[month+1], "1")

elif month == 10 and day != 31:
    print(months[month], day+1)
elif month == 10 and day == 31:
    print(months[month+1], "1")

elif month == 11 and day != 30: 
    print(months[month], day+1)
elif month == 11 and day == 30:
    print(months[month+1], "1")

elif month == 12 and day != 31:
    print(months[month], day+1)
elif month == 12 and day == 31:
    print(months[1], "1")

# Given five integers, print the least of them.
# 10
# 20
# 30
# 40
# 50
#Example output: 10

numlist = []
i = 1

while i <= 5:
	numlist.append(int(input()))
	i += 1
	
#print(numlist)
least = min(numlist)
print(least)

i = 0
while i < 2:
    x1 = int(input())
    y1 = int(input())

    x2 = int(input())
    y2 = int(input())

    x3 = int(input())
    y3 = int(input())

    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1

    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1

    print(x4, y4)
    i += 1
"""
#lst1 = [0,1,2,3,4,5]
#print(type(lst1.sort()))

#d = {"Angel", "Devil"}
#print(type(len(d)))

#lst1 = {1,2,3,4}
#lst2 = {5,6,7,8}
#print(lst1.append(lst2))
#print(lst1 <= lst2)

#lst1 = ["Ian", "Dave", "Billy"]
#print(type(lst1.pop(0)))

def vertical_sum( M ):

     n = len(M)

     m = len(M[0])

     sums = []

     for j in range(0,m):

         sums.append(0)

         for i in range(0,n):
              print(sums)
              sums[len(sums)-1]+=M[i][j]

     return sums

M = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12] ]

print(vertical_sum(M))