def matrix_scaling(M, m, n, c):
    # create a shallow copy of M into the variable M_scaled - this preserves the original
    M_scaled = M.copy()

    # iterate with a range of the number of rows for external loop
    for i in range(m):

        # iterate with a range of the number of columns for internal loop
        for j in range(n):
            # locate the value at [i][j] e.g [0][1] and assign that value to [i][j] * c e.g val at [0][1] * 2
            M_scaled[i][j] = M_scaled[i][j] * c

    # return the copied & changed matrix
    return M_scaled


M = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

print(M)
print(matrix_scaling(M, 3, 4, 2))
print("\n")

M2 = [[1, 2], [3, 4]]
print(M2)
print(matrix_scaling(M2, 2, 2, 0))
print("\n")

M3 = [[1],[2], [3], [4], [5], [6], [7], [8], [9], [10]]
print(M3)
print(matrix_scaling(M3, 10, 1, -1))
print("\n")

M4 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(M4)
print(matrix_scaling(M4, 1, 10, -1))
print("\n")
