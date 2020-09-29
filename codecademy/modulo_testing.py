while True:
    print("Pick first number")
    a = int(input())
    print("Pick second number")
    b = int(input())

    if a== 0 or b == 0:
        print("Cannot divide by zero.")

    elif a % b == 0:
        print("Yes")
    else:
        print("No")
