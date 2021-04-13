
n = int(input())
arr = map(int, input().split())

list1 = list(arr)

# using [:] creates a new object that is a copy of the original list
for i in list1[:]:
    # while iterating over the list if there are duplicate elements remove them
    if list1.count(i) > 1:
        list1.remove(i)

list1.sort()
print(list1[len(list1) - 2])
