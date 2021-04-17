def multiplication_table(n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(j*i, end=" ")
        print("\n")


a, b, = int(input()), int(input())
multiplication_table(a, b)