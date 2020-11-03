"""
Implement a fruitful function scale_matrix(M, m, n, c) that returns the scaled matrix M (where the number at each position is multiplied by c) and does not modify M.

For example, the result of:

M = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
N = scale_matrix(M, 3, 4, 2)
print(M)
print(N)

Must be:
[[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
[[22, 24, 26, 28], [42, 44, 46, 48], [62, 64, 66, 68]]

"""
def scale_matrix(M, m, n, c):                           # Fruitful function required for this task
  result = []                                           # Provide an empty list to start
  
  for i in range(m):                                    # Using the specified value (m) iterate through the number of ROWS
      row = [0] * n                                     # Row is equal to the set of [0] MULTIPLIED by the number of COLUMNS as per specified value (n)
      result.append(row)                                # Append the empty zero set to var result, which is an empty list - this repeats until the end of the rows var

  for j in range(len(M)):                                # iterate through each row using the length of the matrix (list of lists) to control
        #iterate through columns
        for k in range(len(M[0])):                       # iterate through each column in range of the first list in matrix - this will not work if lists are of variable length
            #print(result)
            result[j][k] = M[j][k] * c                   # Assign the the value of the Matrix at coord [j][k] e.g. [1][2] MULTIPLIED by var 'c' (2 in this instance) and loop for each value in matrix    
  
  return result                                          # Function is fruitful so return a value
  
M = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

N = scale_matrix(M, 3, 4, 2)
print(M)
print(N)

"""
def scale_matrix(M, m, n, c):
  N = []                            # Assign an empty list to the var N
  for i in range(0, m):             # Loop using the rows var   
    N.append([])                    # Append [] on the row
    for j in range(0, n):           # Loop J in range of columns var
      N[i].append(M[i][j]*c)        # Var N on row i e.g. N row 0, append the result of M[1][1]*2
      
  return N
"""