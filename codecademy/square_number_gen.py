n = int(input())
counter = 1
while counter * counter < n:
    for counter in range(1,n):
        a = counter * counter
        if a >= n:
            break
        print(a)
