def least_divisor(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i


int1 = int(input())
print(least_divisor(int1))