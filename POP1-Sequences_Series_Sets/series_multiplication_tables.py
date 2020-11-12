rows = int(input())
columns = int(input())
result = 1

for i in range(1, rows + 1):          # Create first loop to print 'rows' value e.g. 5 for 5 iterations
    for j in range(1, columns + 1):   # Create loop to complete multiplication of each row by columns
        result = i * j                # E.g. On Row 1, for value 'i' multiply by 'j'
        print(result, end=" ")        # Print the result of above multiplication
    print("\n")                       # Add a new line after the iteration of internal loop
                                      # Move onto the next 'row'