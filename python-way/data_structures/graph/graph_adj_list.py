"""
can be represent in dict

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

or ...
"""


class AdjListNode:
    def __init__(self, val) -> None:
        self.vertex = val
        self.next = None


class GraphAdjacencyList:
    def __init__(self, edge_count):
        self.V = edge_count
        self.graph = [None] * edge_count

    def add_edge(self, s, d):
        node = AdjListNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjListNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def __str__(self) -> str:
        result = []
        for edge in range(self.V):
            header = f"Vertex {edge}: "
            body = ""
            ptr = self.graph[edge]
            while ptr:
                body += f"{ptr.vertex} -> "
                ptr = ptr.next
            result.append(header + body)
        return "\n".join(result)


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = GraphAdjacencyList(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    print(graph)
