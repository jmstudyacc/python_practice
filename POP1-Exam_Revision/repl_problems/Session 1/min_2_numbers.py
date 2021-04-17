def min_of_two(a, b):
    if a < b:
        return a
    else:
        return b


int1, int2 = [int(input()) for x in range(2)]
print(min_of_two(int1, int2))
