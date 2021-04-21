def print_integers(a, b):
    for i in range(a, b+1):
        print(i, end=" ")


a, b = [int(input()) for x in range(2)]
print_integers(a, b)