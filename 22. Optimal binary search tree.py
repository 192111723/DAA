def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        cost[i][i] = freq[i - 1]
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            cost[i][j] = float('inf')
            total_freq = sum(freq[i - 1:j])
            for r in range(i, j + 1):
                c = cost[i][r - 1] + cost[r + 1][j] + total_freq
                cost[i][j] = min(cost[i][j], c)
    return cost[1][n]
keys = [10, 12, 20]
freq = [34, 8, 50]
print("Cost of optimal BST is", optimal_bst(keys, freq))