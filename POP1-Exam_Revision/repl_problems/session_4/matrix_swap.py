def matrix_swap(M, m, n, i, j):
    # iterate over the matrix by getting the size/len of matrix
    for k in range(0, m):
        # in the matrix swap the indexes of i & j for each iteration of the matrix, k
        M[k][i], M[k][j] = M[k][j], M[k][i]
        # print with a separator, do not return, non-fruitful function
        print(M[k], end=" ")


M1 = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
matrix_swap(M1, 3, 4, 0, 1)
print("\n")
M2 = [[1, 2], [3, 4]]
matrix_swap(M2, 2, 2, 0, 1)
print("\n")
M3 = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
matrix_swap(M3, 10, 1, 0, 0)
print("\n")
M4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]