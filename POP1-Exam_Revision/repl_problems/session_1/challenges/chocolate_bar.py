def choc_bar(n, m, k):
    if k <= n * m:
        if k % n == 0 or k % m == 0:
            return "YES"

    return "NO"


print(choc_bar(4, 2, 6))
print(choc_bar(2, 10, 7))
print(choc_bar(7, 4, 21))
print(choc_bar(7, 1, 6))
print(choc_bar(7, 1, 8))
print(choc_bar(387, 13, 2709))
