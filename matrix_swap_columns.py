"""
Implement the non-fruitful function swap_columns(M, m, n, i, j): 

This modifies the given matrix M, with m rows and n colums, by swapping the (whole) colums i and j.  

M = [   [11, 12, 13, 14], 
        [21, 22, 23, 24], 
        [31, 32, 33, 34]
    ]

swap_columns(M, 3, 4, 0, 1)

print(M)

    [   [12, 11, 13, 14],  
        [22, 21, 23, 24], 
        [32, 31, 33, 34]
    ] 

"""

import copy                                                     # Import the copy library to copy matrix later on in function

def swap_columns(matrix, rows, columns, first_val, second_val): # Non-fruitful function - returns nothing
    M_copy = copy.copy(matrix)                                  # Use copy library to make a new copy of the matrix
    
    # result = []
  
    # This stanza is used to make a new empty Matrix, useful but not needed here
    #for i in range(rows):
    #    row = [0] * columns
    #    result.append(row)

    """
    for j in range(len(matrix)):                                # iterate through each row 
        #iterate through columns
        for k in range(len(matrix[0])):                         # iterate through each column in range of the first list in matrix - this will not work if lists are of variable length
            #print(result)
            result[j][k] = matrix[j][k]                         # Copies the value of matrix[j][k] to result[j][k]
    
    for l in result:
        l[first_val], l[second_val] = l[second_val], l[first_val]
    
    """

    for l in M_copy:
        l[first_val], l[second_val] = l[second_val], l[first_val]
      
    #print(M_copy)
    
M =  [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
swap_columns(M, 3, 4, 0, 1)
print(M)

"""
Model Solution:
---------------
def swap_columns(M, m, n, i, j):
  for row in range(0,m):                    # iterate over for loop with range specified by m var
    temp = M[row][i]                        # create a new var called temp and assign to MATRIX[row][i] e.g MATRIX[1][0]
    M[row][i] = M[row][j]                   # Change MATRIX[row][i] to MATRIX[row][j] e.g to MATRIX[1][1]
    M[row][j] = temp                        # MATRIX[row][j] is assigned to temp
"""