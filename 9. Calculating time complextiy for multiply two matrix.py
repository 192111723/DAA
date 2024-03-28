import time
def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]
start_time = time.time()
result_matrix = multiply_matrices(matrix1, matrix2)
end_time = time.time()
print("Resultant matrix:")
for row in result_matrix:
    print(row)
time_taken = end_time - start_time
print("Time taken for matrix multiplication:", time_taken, "seconds")