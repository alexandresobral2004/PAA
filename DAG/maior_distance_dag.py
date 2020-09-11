# Data structure to store graph edges
class Edge:
    def __init__(self, source, dest, weight):

        self.source = source
        self.dest = dest
        self.weight = weight


# Class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, N):

        # A List of Lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]

        # add edges to the undirected graph
        for edge in edges:
            self.adjList[edge.source].append(edge)


# Perform DFS on graph and set departure time of all
# vertices of the graph
def DFS(graph, v, discovered, departure, time):

    # mark current node as discovered
    discovered[v] = True

    # set arrival time - not needed
    # time = time + 1

    # do for every edge (v -> u)
    for e in graph.adjList[v]:
        u = e.dest
        # u is not discovered
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)

    # ready to backtrack
    # set departure time of vertex v
    departure[time] = v
    time = time + 1

    return time


# The function performs topological sort on a given DAG and then finds out
# the longest distance of all vertices from given source by running
# one pass of Bellman-Ford algorithm on edges of vertices in topological order
def findLongestDistance(graph, source, N):

    # departure stores vertex number having its departure
    # time equal to the index of it
    departure = [-1] * N

    # stores vertex is discovered or not
    discovered = [False] * N
    time = 0

    # perform DFS on all undiscovered vertices
    for i in range(N):
        if not discovered[i]:
            time = DFS(graph, i, discovered, departure, time)

    cost = [float('inf')] * N
    cost[source] = 0

    # Process the vertices in topological order i.e. in order
    # of their decreasing departure time in DFS
    for i in reversed(range(N)):

        # for each vertex in topological order,
        # relax cost of its adjacent vertices
        v = departure[i]

        for e in graph.adjList[v]:
            # edge e from v to u having weight w
            u = e.dest
            w = e.weight * -1  # negative the weight of edge

            # if the distance to the destination u can be shortened by
            # taking the edge vu, then update cost to the lower value
            if cost[v] != float('inf') and cost[v] + w < cost[u]:
                cost[u] = cost[v] + w

    # print longest paths
    for i in range(N):
        print("dist", (source, i), "=", (cost[i] * -1))


if __name__ == '__main__':

    # List of graph edges as per above diagram
    edges = [
        Edge(0, 1, 10), Edge(0, 2, 14), Edge(0, 3, 6),Edge(0, 5, 28), Edge(0, 6, 30), 
        Edge(0, 7, 9), Edge(0, 8, 29), Edge(0, 9, 9), Edge(0, 10, 26), Edge(0, 14, 24), 
        Edge(1, 2, 27), Edge(1, 3, 8), Edge(1, 4, 27), Edge(1, 6, 26), Edge(1, 7, 13), 
        Edge(1, 8, 3), Edge(1, 12, 9), Edge(1, 13, 29), Edge(2, 3, 20), Edge(2, 4, 23), 
        Edge(2, 5, 15), Edge(2, 7, 29), Edge(2, 8, 14), Edge(2, 9, 8), Edge(2, 10, 10), 
        Edge(2, 11, 15), Edge(2, 13, 21), Edge(2, 14, 18), Edge(3, 5, 15), Edge(3, 6, 4),
        Edge(3, 8, 5), Edge(3, 9, 15), Edge(3, 10, 20), Edge(3, 11, 18), Edge(3, 13, 13), 
        Edge(3, 14, 12), Edge(4, 5, 6), Edge(4, 6, 25), Edge(4, 8, 9), Edge(4, 9, 28), 
        Edge(4, 10, 28), Edge(4, 11, 1), Edge(4, 12, 18), Edge(4, 13, 15), Edge(4, 14, 16), 
        Edge(5, 6, 11), Edge(5, 8, 24), Edge(5, 9, 8), Edge(5, 10, 5), Edge(5, 11, 11), 
        Edge(5, 12, 30), Edge(5, 13, 8), Edge(6, 7, 25), Edge(6, 10, 19), Edge(6, 11, 18), 
        Edge(6, 12, 20), Edge(6, 13, 19), Edge(7, 8, 23), Edge(7, 10, 17), Edge(7, 11, 30), 
        Edge(7, 12, 13), Edge(7, 14, 25), Edge(8, 9, 28), Edge(8, 10, 1), Edge(9, 10, 28), 
        Edge(9, 11, 11), Edge(9, 12, 10), Edge(9, 13, 15), Edge(9, 14, 20), Edge(10, 12, 10), 
        Edge(10, 14, 16), Edge(11, 14, 6), Edge(12, 13, 10),Edge(12, 14, 1), Edge(13, 14, 12)
    ]

    # Set number of vertices in the graph
    N =15

    # create a graph from given edges
    graph = Graph(edges, N)

    # source vertex
    source = 0

    # find longest distance of all vertices from given source
    findLongestDistance(graph, source, N)
