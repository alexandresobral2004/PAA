# Class to represent a graph object
class Graph:
	# Constructor
	def __init__(self, edges, N):

		# A List of Lists to represent an adjacency list
		self.adjList = [[] for _ in range(N)]

		# add edges to the undirected graph
		for (src, dest) in edges:
			self.adjList[src].append(dest)


# Perform DFS on graph and set departure time of all vertices of the graph
def DFS(graph, v, discovered, departure, time):

	# mark current node as discovered
	discovered[v] = True

	# do for every edge (v -> u)
	for u in graph.adjList[v]:
		# u is not discovered
		if not discovered[u]:
			time = DFS(graph, u, discovered, departure, time)

	# ready to backtrack
	# set departure time of vertex v
	departure[v] = time
	time = time + 1

	return time


# returns true if given directed graph is DAG
def isDAG(graph, N):

	# stores vertex is discovered or not
	discovered = [False] * N

	# stores departure time of a vertex in DFS
	departure = [None] * N

	time = 0

	# Do DFS traversal from all undiscovered vertices
	# to visit all connected components of graph
	for i in range(N):
		if not discovered[i]:
			time = DFS(graph, i, discovered, departure, time)

	# check if given directed graph is DAG or not
	for u in range(N):

		# check if (u, v) forms a back-edge.
		for v in graph.adjList[u]:

			# If departure time of vertex v is greater than equal
			# to departure time of u, then they form a back edge

			# Note that departure[u] will be equal to departure[v]
			# only if u = v i.e vertex contain an edge to itself
			if departure[u] <= departure[v]:
				return False

	# no back edges
	return True


# Check if given digraph is a DAG (Directed Acyclic Graph) or not
if __name__ == '__main__':

	# List of graph edges as per above diagram
	edges = [(0, 1), (0, 2), (0, 4), (0, 5), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 14), (1, 2), (1, 3), (1, 5), (1, 7), (1, 8), (1, 9), (1, 10), (1, 13), (1, 14), (2, 3), (2, 4), (2, 5), (2, 7), (2, 11), (2, 13), (3, 4), (3, 5), (3, 6), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 14), (4, 5), (4, 7), (4, 8), (4, 10), (4, 11), (4, 12), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (6, 7), (6, 8), (6, 9), (6, 12), (6, 14), (7, 8), (7, 10), (8, 9), (8, 11), (8, 12), (8, 13), (9, 10), (10, 11), (10, 13), (11, 13), (11, 14), (13, 14)]

	# Set number of vertices in the graph
	N = 15

	# create a graph from given edges
	graph = Graph(edges, N)

	# check if given directed graph is DAG or not
	if isDAG(graph, N):
		print("Graph is DAG")
	else:
		print("Graph is not DAG")
