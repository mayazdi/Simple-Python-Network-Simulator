import time

class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.nodes_dic = {}
		self.netwk_dic = {}
		self.graph = []
	
	def add_node_to_dic(self, val, i):
		self.nodes_dic[val] = i

	def get_network_adjs(self, net):
		return self.nodes_dic[self.netwk_dic[net][0]], self.nodes_dic[self.netwk_dic[net][1]]
	
	def get_nodes_dic(self):
		return self.nodes_dic

	def get_netwk_dic(self):
		return self.netwk_dic

	def addNetwork(self, net_addr, nd1, nd2):
		self.netwk_dic[net_addr] = (nd1, nd2)
	
	def addEdge(self, nd1, nd2):
		self.graph.append([self.nodes_dic[nd1], self.nodes_dic[nd2]])
		self.graph.append([self.nodes_dic[nd2], self.nodes_dic[nd1]])

	def get_distances_from(self, net_selected):
		nd1, nd2 = self.get_network_adjs(net_selected)
		ls1 = self.BellmanFord(nd1)
		ls2 = self.BellmanFord(nd2)
		final_adj = []
		for i in range(self.V):
			final_adj.append(min(ls1[i], ls2[i]))
		return final_adj

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

		# self.printArr(dist)
		return dist



def print_seperator():
	print("----------------------------")


print("Enter the graph Size:")
ln = input()
g = Graph(int(ln))
nodes = []

print("Deafult Names(R0, R1, ..., R(n-1))?[Y/n]")
default_names = input()
if default_names=="Y" or default_names=="Yes" or default_names=="":
	for i in range(int(ln)):
		val = "R" + str(i)
		nodes.append(val)
		g.add_node_to_dic(val, i)
else:
	print("Enter the values then:")
	for i in range(int(ln)):
		print(str(i) + ":", end="")
		val = input()
		nodes.append(val)
		g.add_node_to_dic(val, i)

print("names: " + str(nodes))
print(g.get_nodes_dic())
print_seperator()
print("Enter the graph topology in the following format:\nNode1 Node2 (XXX.XXX.XXX.XXX)\n")
for i in range(0, int(ln)):
    print("{count}:".format(count=i+1), end="")
    edge = input()
    nd1, nd2, net_addr = edge.split(' ')
    g.addEdge(nd1, nd2)
    g.addNetwork(net_addr, nd1, nd2)

print_seperator()

i = 0
NK = g.get_netwk_dic().keys()
for item in NK:
	print(str(i)+":"+item)
	i+=1
print("Pick a Network from above.\n>>", end="")
net_selected=input()
g.printArr(g.get_distances_from(net_selected))
