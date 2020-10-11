
sum = 0     # Initiate sum variable

while True:                 # Create loop
    num = int(input())      # Initiate num var
    sum += num              # Sum is equal to sum + num
    if num == 0:            # if num == 0
        break               # then break

print(sum)