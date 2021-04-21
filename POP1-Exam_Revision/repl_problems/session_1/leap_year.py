def leap_year(n):
    if n % 4 == 0 and n % 100 != 0:
        return "LEAP"
    elif n % 400 == 0:
        return "LEAP"
    else:
        return "COMMON"


year = int(input())
print(leap_year(year))