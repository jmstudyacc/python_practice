
n = float(input())    # specify float as will be using decimals

m = n % 1             # use modulus 1 to find the decimal remainder of quotient (still not really sure WHY this works)
m = round(m, 3)       # as per the exercise guidance this helps resolve any issues around binary approximation of fractions

print(m)