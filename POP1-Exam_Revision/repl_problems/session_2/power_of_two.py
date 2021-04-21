def power_of_two(n):
    for i in range(n-1, 0, -1):
        # did not use ** - instead used the pow() method
        if pow(2, i) <= N:
            return f"{i} {pow(2, i)}"


N = int(input())
print(power_of_two(N))