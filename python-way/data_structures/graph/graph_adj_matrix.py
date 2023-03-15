"""
a graph is a data structure (V, E) that consists of

- collection of vertices V
- collection of edges E, represented as ordered pairs of vertices (u,v)

graph view:

0---3
|\
| 2
|/
1

graph in terms V, E

V = {0, 1, 2, 3}
E = {(0,1), (0,2), (0,3), (1,2)}
G = {V, E}

graph term:
- Adjacency: A vertex is said to be adjacent to another vertex if there is an edge connecting them.
    Vertices 2 and 3 are not adjacent because there is no edge between them.
- Path: A sequence of edges that allows you to go from vertex A to vertex B is called a path.
    0-1, 1-2 and 0-2 are paths from vertex 0 to vertex 2.
- Directed Graph: A graph in which an edge (u,v) doesn't necessarily mean that there is an edge (v, u) as well.
    The edges in such a graph are represented by arrows to show the direction of the edge.

Graph Representation:

Graphs are commonly represented in two ways:
1. Adjacency Matrix
    An adjacency matrix is a 2D array of V x V vertices. Each row and column represent a vertex.
    If the value of any element a[i][j] is 1, it represents that there is an edge connecting vertex i and vertex j.

    Since it is an undirected graph, for edge (0,2), we also need to mark edge (2,0);
        making the adjacency matrix symmetric about the diagonal.

    Edge lookup(checking if an edge exists between vertex A and vertex B) is extremely fast in
        adjacency matrix representation but we have to reserve space for every possible link between all vertices(V x V),
        so it requires more space.

2. Adjacency List

    An adjacency list represents a graph as an array of linked lists.
    The index of the array represents a vertex and each element in its linked list represents
        the other vertices that form an edge with the vertex.
    An adjacency list is efficient in terms of storage because we only need to store the values for the edges.
        For a graph with millions of vertices, this can mean a lot of saved space.
"""


class GraphAdjacencyMatrix:
    def __init__(self, count_nodes):
        self.adj_matrix = [[0] * count_nodes for _ in range(count_nodes)]
        self.size = count_nodes

    def add_edge(self, v1, v2):
        if v1 == v2:
            print(f"same vertex {v1} and {v2}")
        self.adj_matrix[v1][v2] = self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adj_matrix[v1][v2] == 0:
            print(f"not edge between {v1} and {v2}")
            return
        self.adj_matrix[v1][v2] = self.adj_matrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def __str__(self):
        result = []
        for row in self.adj_matrix:
            result.append("  ".join(map(str, row)))
        return "\n".join(result)


if __name__ == "__main__":
    g = GraphAdjacencyMatrix(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    print("adjacency matrix:", g, sep="\n")