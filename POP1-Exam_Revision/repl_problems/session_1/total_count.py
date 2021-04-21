def total_cost(A, B, N):
    result = ((A*100) + B) * N
    return f"{result // 100}\n{result % 100}"


A, B, N = [int(input()) for x in range(3)]
print(total_cost(A, B, N))