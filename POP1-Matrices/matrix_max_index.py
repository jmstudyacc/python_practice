"""
M = [   [0, 3, 2, 4], 
        [2, 3, 5, 5],  
        [5, 1, 2, 3]
    ]
"""

"""
Implement a function matrix_max_index(M, m, n) that returns a tuple (i,j) where i is the row number and j is the column number of the maximal element of the martix. The arguments of the function are:

     M - the matrix of numbers (represented as usual by a list of lists)
     m - the number of rows in M
     n - the number of columns in M  


If there exist multiple such elements in different rows, print the one with smaller row number. If there multiple such elements occur on the same row, output the smallest column number. 
"""
"""
def matrix_max_index(M, m, n):
    count = 0

    for i in range(m):
        row_max = max(M[i])

        #print("\nRow,", i, M[i])
        #print("The MAX element of the row is:", row_max)
        #print("The INDEX of the MAX in this row:", max_coord)

        if row_max > count:                                                 # If the row_max value is greater than the count value
            count = row_max                                                 # Assign the new count value to be the row_max
            max_ind = M[i].index(row_max)                                   # Find the index of this value in the loop, using the list.index() method
            max_coord = []                                                  # Create an empty list
            max_coord.extend((i, max_ind))                                  # Add 'i', which is the row number and the index of the max value
            
            #print("The MAX value is:", count)
            #print("The COORDS of this value:", max_coord)

    return tuple(max_coord)                                                 # Tuple is requested as output, so convert to Tuple

M = [[1, 4, 5, 2, 7], [3, 4, 8, 0, 8], [8, 8, 8, 8, 8]]

print(matrix_max_index(M, 3, 5))

"""
# MODEL ANSWER
def  matrix_max_index(M, m, n):
  i_max = 0                                         # Assign a max to the 'ith' row
  j_max = 0                                         # Assign a max to the 'jth' row
  for i in range(0,m):                              # Loop over the 'ith' rows
    for j in range(0,n):                            # Loop over the 'jth' columns in the 'ith' rows
      if M[i][j] > M[i_max][j_max]:                 # If VALUE at M[i][j] greater than VALUE at M(i_max, j_max) e.g. VALUE at (0,1) is GREATER than VALUE at (0,0)  
        i_max = i                                   # Set 'i_max' VALUE to current VALUE of 'i' - ROWS
        j_max = j                                   # Set 'j_max' VALUE to current VALUE of 'j' - COLUMNS
      
  return (i_max, j_max)                             # Return the value of i_max and j_max
