import time, threading
from threading import Thread

class Graph:
	def __init__(self, vertices, ri):
		self.refresh_interval = ri
		self.V = vertices
		self.network_ports = {}
		self.nodes_dic = {}
		self.netwk_dic = {}
		self.graph = []
	

	def add_nn_port(self, key, port):
		self.network_ports[key] = port

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
	
	
	def call_bellmanford(self):
		ticker = threading.Event()
		while not ticker.wait(self.refresh_interval):
			g.BellmanFord(0)

	def BellmanFord(self, src):

		dist = [float("Inf")] * self.V
		dist[src] = 0

		for _ in range(self.V - 1):
			for u, v in self.graph:
				if dist[u] != float("Inf") and dist[u] + 1 < dist[v]:
						dist[v] = dist[u] + 1

		return dist



def print_seperator():
	print("----------------------------")


print("Enter the Refresh Interval:")
ref_interval = input()
print("Enter the graph Size:")
ln = input()
g = Graph(int(ln), int(ref_interval))
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
print("Networks Count:", end="")
net_len = input()
print("Enter the graph topology in the following format:\nNode1 Node2 PN1 PN2 (XXX.XXX.XXX.XXX)\n")
for i in range(0, int(net_len)):
    print("{count}:".format(count=i+1), end="")
    edge = input()
    nd1, nd2, pn1, pn2, net_addr = edge.split(' ')
    g.add_nn_port((nd1, net_addr), int(pn1))
    g.add_nn_port((nd2, net_addr), int(pn2))
    g.addEdge(nd1, nd2)
    g.addNetwork(net_addr, nd1, nd2)


t2 = Thread(target=g.call_bellmanford)
t2.setDaemon(True)
t2.start()

action = ["quit", "add", "remove", "report", "change interval", "report router"]
while True:
	print_seperator()
	print("Take one of the actions below:")
	print(action)
	print_seperator()
	mode = input()
	if mode==action[0]:
		break
	elif mode==action[1]:
		edge = input()
		nd1, nd2, net_addr = edge.split(' ')
		g.addEdge(nd1, nd2)
		g.addNetwork(net_addr, nd1, nd2)
	elif mode==action[2]:
		print("remove a network")
	elif mode==action[3]:
		i = 0
		NK = g.get_netwk_dic().keys()
		for item in NK:
			print(str(i)+":"+item)
			i+=1
		print("Pick a Network from above.\n>>", end="")
		try:
			net_selected=input()
			# The exact same network
			g.printArr(g.get_distances_from(net_selected))
			# g.printArr(g.get_distances_from(net_selected))
		except:
			print("Couldn't investigate that network")
	elif mode==action[4]:
		g.refresh_interval=int(input())
	elif mode==action[5]:
		pass
	else:
		print("Action Not Valid!")	
