# M =[    [0, 3, 2, 4],
#        [2, 3, 5, 5],  
#        [5, 1, 2, 3]
#    ]

# 1
"""
# Finding MAX values in the lists
#R1_max = max(M[0])
#R2_max = max(M[1])
#R3_max = max(M[2])

#print(R1_max)
#print(R2_max)
#print(R3_max)

# Printing INDEX of MAX values
#print(M[0].index(R1_max))
#print(M[1].index(R2_max))
#print(M[2].index(R3_max))

# Reporting INDEX positions
#print("\nM is equal to:", M)

#print("\nM[1] is equal to:", M[1])
#print("M[1][2] is equal to:", M[1][2])

#print("\nLast value of 1st row:", M[0][-1])
#print("Last value of last row:", M[-1][-1])
"""

# 2
"""
# Finding a specific column
column = []

for row in M:
    column.append(row[2])

print("\n3rd column is:", column)

"""

# 3
"""
# Printing a Table out from the Matrix
for i in range(len(M)):
    # Process the 'i-th' row
    for j in range(4):
        # Process the 'j-th' column in the 'i-th' row
        print("%8d" % M[i][j], end= " ")        # Individual elements in a table are accessed by using two index values table[i][j]
    print()

"""
M = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]


def swap_columns(M, m, n, i, j):
    result = []

    for z in range(m):
        row = [0] * n
        result.append(row)

    # iterate through rows
    for m in range(len(M)):
        # iterate through columns
        for n in range(len(M[0])):
            result[i][j] = M[i][j]

    for l in result:
        l[i], l[j] = l[j], l[i]
        print(l)


print(swap_columns(M, 3, 4, 0, 1))
print(M)
