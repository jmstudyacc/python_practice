num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == num2: 
    if num1 == num3:
        print(3)
    else:
        print(2)
elif num1 == num3 or num2 == num3:
  print(2)
else:
  print(0)
