def split_matrix(matrix):
    n = len(matrix)
    n2 = n // 2
    A = [row[:n2] for row in matrix[:n2]]
    B = [row[n2:] for row in matrix[:n2]]
    C = [row[:n2] for row in matrix[n2:]]
    D = [row[n2:] for row in matrix[n2:]]
    return A, B, C, D
def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1))]
def subtract_matrices(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1))]
def strassen_multiply(matrix1, matrix2):
    n = len(matrix1)
    if n <= 2:
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result
    else:
        A, B, C, D = split_matrix(matrix1)
        E, F, G, H = split_matrix(matrix2)
        P1 = strassen_multiply(A, subtract_matrices(F, H))
        P2 = strassen_multiply(add_matrices(A, B), H)
        P3 = strassen_multiply(add_matrices(C, D), E)
        P4 = strassen_multiply(D, subtract_matrices(G, E))
        P5 = strassen_multiply(add_matrices(A, D), add_matrices(E, H))
        P6 = strassen_multiply(subtract_matrices(B, D), add_matrices(G, H))
        P7 = strassen_multiply(subtract_matrices(A, C), add_matrices(E, F))
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = P5[i][j] + P4[i][j] - P2[i][j] + P6[i][j]
                result[i][j + n//2] = P1[i][j] + P2[i][j]
                result[i + n//2][j] = P3[i][j] + P4[i][j]
                result[i + n//2][j + n//2] = P5[i][j] + P1[i][j] - P3[i][j] - P7[i][j]
        return result
matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix2 = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]
result = strassen_multiply(matrix1, matrix2)
for row in result:
    print(row)