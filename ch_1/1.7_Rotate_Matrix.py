def rotate_matrix(matrix):
    # fetch the length of rows and columns
    n = len(matrix)
    result = []
    for row in range(n):
        for col in range(n):
            result[col][n - 1 - row] = matrix[row][col]

    return result

m1 = [[1, 2], [3, 4]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(m1, "-->", rotate_matrix(m1), '\n')
print(m2, "-->", rotate_matrix(m2), '\n')