def three_digits(n):
    result = (n // 100) + (n % 100 // 10) + (n % 10)
    return result


a = int(input())

print(three_digits(a))



