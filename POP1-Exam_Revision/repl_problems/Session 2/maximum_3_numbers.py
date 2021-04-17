def max_three(num1, num2, num3):
    maxi = max(num1, num2, num3)
    print(maxi)


a, b, c = [int(input()) for x in range(3)]

max_three(a, b, c)
