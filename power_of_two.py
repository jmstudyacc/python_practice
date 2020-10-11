n = int(input())

counter = 1     
expo = 1
base = 2

for i in range(1, n):       # Begin 'for loop', value of 'i' is used for exponent of base value
    total = base ** i       # Base value (2) to the power of 'i'
    counter = total         # Assign total to 'counter' for the proceeding test
    if counter > n:         # 'If statement' to test if 'counter' has a value that breaks the test
        i -= 1              # Minus 1 from 'i' value to get the previous value of 'i'
        total = base ** i   # Recalculate the value of total with new/old value of 'i'
        print(i, total)     # print 'i' and 'total' values
        break

"""
while counter <= n:             # while loop with test condition
    expo += 1                   # increment the exponent value to emulate 2^1, 2^2
    counter = base ** expo      # counter variable used to store the value of 2^expo
    if counter > n:             # test condition with if to act if counter is higher than n
        expo -= 1               # without this the expo variable would grow too large before while loop ends
        counter = base ** expo  # with the new(old) expo value calculate the counter value again
        break                   # break as the greater than n condition met 

print(expo, counter)
"""
"""
looping = False

while not looping:   
    if base ** expo > n:
        counter = base ** expo
        looping = True
        break

    x = expo
    total = base ** x 

    if base ** expo <= n:
        counter = base ** expo

    expo += 1

print(x, total)
"""