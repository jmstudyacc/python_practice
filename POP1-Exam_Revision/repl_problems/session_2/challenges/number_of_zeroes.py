def num_of_zeroes():
    total = 0
    n = int(input())
    for i in range(n):
        m = int(input())
        if m == 0:
            total += 1

    return total


print(num_of_zeroes())
