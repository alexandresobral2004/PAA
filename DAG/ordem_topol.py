# Class to represent a graph object
class Graph:
	def __init__(self, edges, N):

		# A List of Lists to represent an adjacency list
		self.adjList = [[] for _ in range(N)]

		# add edges to the undirected graph
		for (src, dest) in edges:

			# add an edge from source to destination
			self.adjList[src].append(dest)


# Perform DFS on graph and set departure time of all
# vertices of the graph
def DFS(graph, v, discovered, departure, time):

	# mark current node as discovered
	discovered[v] = True

	# set arrival time
	time = time + 1

	# do for every edge (v -> u)
	for u in graph.adjList[v]:
		# u is not discovered
		if not discovered[u]:
			time = DFS(graph, u, discovered, departure, time)

	# ready to backtrack
	# set departure time of vertex v
	departure[time] = v
	time = time + 1

	return time


# performs Topological Sort on a given DAG
def doTopologicalSort(graph, N):

	# departure stores the vertex number using departure time as index
	departure = [-1] * 2 * N

	# Note if we had done the other way around i.e. fill the
	# list with departure time by using vertex number
	# as index, we would need to sort the list later

	# stores vertex is discovered or not
	discovered = [False] * N
	time = 0

	# perform DFS on all undiscovered vertices
	for i in range(N):
		if not discovered[i]:
			time = DFS(graph, i, discovered, departure, time)

	# Print the vertices in order of their decreasing
	# departure time in DFS i.e. in topological order
	for i in reversed(range(2 * N)):
		if departure[i] != -1:
			print(departure[i], end=' ')


# Topological Sort Algorithm for a DAG using DFS
if __name__ == '__main__':

	# List of graph edges as per above diagram
	edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7, ),(0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14)]

	# Set number of vertices in the graph
	N = 15

	# create a graph from edges
	graph = Graph(edges, N)

	# perform Topological Sort
	doTopologicalSort(graph, N)
