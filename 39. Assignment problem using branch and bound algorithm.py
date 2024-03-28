import numpy as np
from itertools import permutations
def reduce_matrix(matrix):
    row_min = np.min(matrix, axis=1)
    matrix -= row_min[:, np.newaxis]
    col_min = np.min(matrix, axis=0)
    matrix -= col_min
    return matrix
def cost_of_assignment(assignment, cost_matrix):
    total_cost = 0
    for i, j in enumerate(assignment):
        total_cost += cost_matrix[i, j]
    return total_cost
def assign_jobs(cost_matrix):
    n = cost_matrix.shape[0]
    min_cost = float('inf')
    min_assignment = None
    reduced_matrix = reduce_matrix(cost_matrix)
    unassigned_jobs = list(range(n))
    for perm in permutations(range(n)):
        assignment = []
        total_cost = 0
        for i in range(n):
            total_cost += reduced_matrix[i, perm[i]]
            assignment.append((i, perm[i]))
        if total_cost < min_cost:
            min_cost = total_cost
            min_assignment = assignment
    return min_assignment, min_cost
cost_matrix = np.array([[5, 4, 2, 7],
                        [2, 1, 5, 6],
                        [4, 3, 2, 1],
                        [3, 2, 1, 4]])
assignment, min_cost = assign_jobs(cost_matrix)
print("Minimum cost of assignment:", min_cost)
print("Assignment:", assignment)