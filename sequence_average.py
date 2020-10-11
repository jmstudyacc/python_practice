
sum = 0     # Initialise sum variable
count = 0   # Initialise the count var

while True:                 # Create loop
    num = int(input())      # Initiate num var
    sum += num              # Sum is equal to sum + num

    if num == 0:            # if num == 0
        break               # then break
    
    count += 1              # Increment count by 1 if num does not equal 0

print(sum)
print(sum // count)