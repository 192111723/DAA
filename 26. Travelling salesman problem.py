import itertools
def tsp(graph):
    n = len(graph)
    min_distance = float('inf')
    for perm in itertools.permutations(range(n)):
        distance = 0
        for i in range(n):
            distance += graph[perm[i - 1]][perm[i]]
        min_distance = min(min_distance, distance)
    return min_distance
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
min_distance = tsp(graph)
print("Minimum distance for TSP:", min_distance)