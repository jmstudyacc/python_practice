# Practising using Matrix or Table

M =  [[0, 3, 2, 4], [2, 3, 5, 5], [5, 1, 2, 3]]

ROWS = 3
COLUMNS = 4
for i in range(ROWS):
    # Process the 'i-th' row
    for j in range(COLUMNS):
        # Process the 'j-th' column in the 'i-th' row
        print("%8d" % M[i][j], end= " ")               # Individual elements in a table are accessed by using two index values table[i][j]
    print()

print(M[1][0] + M[0][0] + M[2][0], end=" ")

"""
# Assign a number of rows
ROWS = 3

# Assign number of columns
COLUMNS = 4

# Create a new list to hold values
table = []

# For loop to create the list
for item in range(ROWS):
    row = [0] * COLUMNS                     # This is not the integer, 0, this is a list item of 0, [0], use the * to add additional Int '0' elements
    table.append(row)

print(table)
"""
"""
count = 1

for i in M:
    print(f"\nThis is iteration {count} over M")
    count += 1
    for j in i:
        print(j, end=" ")
"""
