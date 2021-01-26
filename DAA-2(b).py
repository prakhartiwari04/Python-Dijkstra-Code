from heapq import heappop, heappush
 
 
# Data structure to store graph edges
class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight
 
 
# data structure to store heap nodes
class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
 
    def __lt__(self, other):
        return self.weight < other.weight
 
 
# class to represent a graph object
class Graph:
    def __init__(self, edges, N):
        self.adj = [[] for _ in range(N)]
        for edge in edges:
            self.adj[edge.source].append(edge)
 
 
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)
 
 

def shortest_path(graph, source, no_of_vertices):
 
    pq = []
    heappush(pq, Node(source, 0))
 
    # set infinite distance from source to v initially
    dist = [float('inf')] * no_of_vertices
    dist[source] = 0
 
    done = [False] * no_of_vertices
    done[source] = True
 
    prev = [-1] * no_of_vertices
    route = []
 
    while pq:
 
        node = heappop(pq)          
        u = node.vertex             
 
        for edge in graph.adj[u]:
            v = edge.dest
            weight = edge.weight
 
            # Relaxation step
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))
 

        done[u] = True
 
    for i in range(1, no_of_vertices):
        if i != source and dist[i] != float('inf'):
            get_route(prev, i, route)
            print(f"Path ({source} -> {i}): Minimum Cost = {dist[i]}, Route = {route}")
            route.clear()
 
 
if __name__ == '__main__':
 
    # (u, v, w) triplet represent undirected edge from
    # vertex u to vertex v having weight w
    edges = [Edge(0, 1, 10), Edge(0, 4, 3), Edge(1, 2, 2),
             Edge(1, 4, 4), Edge(2, 3, 9), Edge(3, 2, 7),
             Edge(4, 1, 1), Edge(4, 2, 8), Edge(4, 3, 2)]
 
    # Set number of vertices in the graph
    no_of_vertices = 5
    graph = Graph(edges, no_of_vertices)
 
    source = 0
    shortest_path(graph, source, no_of_vertices)