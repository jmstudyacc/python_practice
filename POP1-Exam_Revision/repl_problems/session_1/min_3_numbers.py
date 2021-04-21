def min_of_three(a, b, c):
    list1 = [a, b, c]
    list1.sort()
    return list1[0]


int1, int2, int3 = [int(input()) for x in range(3)]
print(min_of_three(int1, int2, int3))
