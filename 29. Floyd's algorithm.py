INF = float('inf')
def floyd_warshall(graph):
    n = len(graph)
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
graph = [
    [0, 3, 8, INF, -4],
    [-1, 0, -2, 1, 7],
    [INF, 4, 0, INF, -1],
    [2, INF, -5, 0, INF],
    [INF, INF, INF, 4, 0]
]
shortest_paths = floyd_warshall(graph)
for row in shortest_paths:
    print(row)