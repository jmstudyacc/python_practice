
max = 0     # Initialise max var to store num values

while True:                 # Create loop
    num = int(input())      # Initiate num var

    if num == 0:            # if num == 0
        break               # then break

    elif num > max:         # if above test is satisified check if num is greater than current value of max
        max = num           # if num is bigger then assign num to max

print(max)