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
        self.adj_matrix = [
            [0] * count_nodes for _ in range(count_nodes)
        ]
        self.size = count_nodes

    
