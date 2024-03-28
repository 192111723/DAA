class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    def is_safe(self, v, pos, path):
        if self.graph[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True
    def hamiltonian_circuit_util(self, path, pos):
        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            return False
        for v in range(1, self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.hamiltonian_circuit_util(path, pos + 1):
                    return True
                path[pos] = -1
        return False
    def hamiltonian_circuit(self):
        path = [-1] * self.V
        path[0] = 0
        if not self.hamiltonian_circuit_util(path, 1):
            print("No Hamiltonian circuit exists")
            return False
        print("Hamiltonian circuit exists and the path is:")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0])
        return True
g = Graph(5)
g.graph = [[0, 1, 0, 1, 0],
           [1, 0, 1, 1, 1],
           [0, 1, 0, 0, 1],
           [1, 1, 0, 0, 1],
           [0, 1, 1, 1, 0]]
g.hamiltonian_circuit()