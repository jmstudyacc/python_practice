
greaterVal = 0              # empty int variable to count result
num = int(input())          # Initialise first value outside of loop
holdVal = num               # First value of holdVal is defined outside of loop

while True:                 
    num = int(input())      # Reassigns value of num via a loop 
    
    if num == 0:            # if num == 0
        break               # then break

    elif num > holdVal:     # if above test is satisified check if num is greater than holdVal
        greaterVal += 1     # Increment greaterVal by 1 if check is satisfied

    holdVal = num           # After tests and conditions reassign holdVal to the num value assigned in this loop iteration
    
print(greaterVal)