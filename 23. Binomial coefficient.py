def binomial_coefficient(n, k):
    C = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]
n = 5
k = 2
print("Binomial coefficient C({}, {}) = {}".format(n, k, binomial_coefficient(n, k)))