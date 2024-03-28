def prim_mst(graph):
    mst = []
    visited = set()
    visited.add(0)
    while len(visited) < len(graph):
        min_weight = float('inf')
        min_edge = None
        for u in visited:
            for v, weight in graph[u]:
                if v not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (u, v, weight)
        if min_edge:
            mst.append(min_edge)
            visited.add(min_edge[1])
    return mst
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}
mst = prim_mst(graph)
print("Edges in the Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} (weight: {edge[2]})")