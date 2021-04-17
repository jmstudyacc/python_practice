def list_squares(n):
    if n == 1:
        print("1")
    else:
        for i in range(1, n):
            if i ** 2 <= n:
                print(i**2, end=" ")
            else:
                break


N = int(input())
list_squares(N)
