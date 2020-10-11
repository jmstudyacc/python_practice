threeDigit = int(input())
countDigit = len(str(threeDigit))

if countDigit == 3:
    unitDigit = threeDigit % 10
    #print(unitDigit)

    tenDigit = (threeDigit // 10 ) % 10
    #print(tenDigit)

    hundredDigit = (threeDigit // 100)
    #print(hundredDigit)

    sumDigits = unitDigit + tenDigit + hundredDigit
    print(sumDigits)

else:
    print("Error: Please enter 3 digits.")