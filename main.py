class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = []

	def addEdge(self, u, v):
		self.graph.append([u, v])
		self.graph.append([v, u])

	def printArr(self, dist):
		print("Vertex Distance from Source")
		for i in range(self.V):
			print("{0}\t\t{1}".format(i, dist[i]))
	
	def BellmanFord(self, src):

		dist = [float("Inf")] * self.V
		dist[src] = 0

		for _ in range(self.V - 1):
			for u, v in self.graph:
				if dist[u] != float("Inf") and dist[u] + 1 < dist[v]:
						dist[v] = dist[u] + 1

		# for u, v in self.graph:
		# 		if dist[u] != float("Inf") and dist[u] + 1 < dist[v]:
		# 				print("Graph contains negative weight cycle")
		# 				return
		
		self.printArr(dist)


def print_seperator():
	print("----------------------------")



print("Enter the graph Size:")
ln = input()
li = []
nodes = []
nodes_dic = {}
netwk_dic = {}

print("Deafult Names(R0, R1, ..., R(n-1))?[Y/n]")
default_names = input()
if default_names=="Y" or default_names=="Yes" or default_names=="":
	for i in range(int(ln)):
		val = "R" + str(i)
		nodes.append(val)
		nodes_dic[val] = i
else:
	print("Enter the values then:")
	for i in range(int(ln)):
		print(str(i) + ":", end="")
		val = input()
		nodes.append(val)
		nodes_dic[val] = i

print("names: " + str(nodes))
print(nodes_dic)
print_seperator()
print("Enter the graph topology in the following format:\nNode1 Node2 (XXX.XXX.XXX.XXX)\n")
for i in range(0, int(ln)):
    print("{count}:".format(count=i+1), end="")
    edge = input()
    nd1, nd2, net_addr = edge.split(' ')
    netwk_dic[net_addr] = (nd1, nd2)

print_seperator()
#do all the routing things
g = Graph(5)
g.addEdge(0, 1)
g.addEdge(2, 1)
g.addEdge(3, 1)
g.addEdge(3, 4)
g.addEdge(2, 3)

g.BellmanFord(0)

print_seperator()
i = 0
netwk_dic.keys()
for item in netwk_dic.keys():
	print(str(i)+":"+item)
	i+=1
print("Pick a Network from above.\n>>", end="")
net_selected=input()
print(netwk_dic[net_selected])
