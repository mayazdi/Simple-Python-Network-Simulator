class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = []

	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	def printArr(self, dist):
		print("Vertex Distance from Source")
		for i in range(self.V):
			print("{0}\t\t{1}".format(i, dist[i]))
	
	def BellmanFord(self, src):

		dist = [float("Inf")] * self.V
		dist[src] = 0

		for _ in range(self.V - 1):

			for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
						dist[v] = dist[u] + w

		for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
						print("Graph contains negative weight cycle")
						return
		
		self.printArr(dist)




print("Enter the graph Size:")
ln = input()
li = []
print("Enter the graph topology in the following format:\n(XXX.XXX.XXX.XXX)\n")
for i in range(0, int(ln)):
    print("{count}:".format(count=i+1), end="")
    li.append(input())

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.BellmanFord(0)
