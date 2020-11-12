
n = int(input())

result = 1

for i in range(1, n + 1):
    result *= i                 # result starts as 1x1=1, then becomes 2x1=2, then becomes 3x2=6, 4x6=24
    print(result, end= "   ")

print(result)