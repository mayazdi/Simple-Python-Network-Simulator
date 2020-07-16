import time, threading
from threading import Thread


class Graph:
    def __init__(self, vertices, ri):
        self.refresh_interval = ri
        self.V = vertices
        self.network_ports = {}
        self.nodes_dic = {}
        self.network_dic = {}
        self.node_to_network = {}
        self.graph = []

    def add_network_node_port(self, key, port):
        self.network_ports[key] = port

    def add_node_to_dic(self, val, i):
        self.nodes_dic[val] = i

    def get_network_adjs(self, net):
        return self.nodes_dic[self.network_dic[net][0]], self.nodes_dic[self.network_dic[net][1]]

    def get_nodes_dic(self):
        return self.nodes_dic

    def get_network_dic(self):
        return self.network_dic

    def add_node(self, net_addr, network_dic1, network_dic2):
        try:
            self.node_to_network[self.nodes_dic[network_dic1]].append(net_addr)
        except:
            self.node_to_network[self.nodes_dic[network_dic1]] = []
            self.node_to_network[self.nodes_dic[network_dic1]].append(net_addr)
        try:
            self.node_to_network[self.nodes_dic[network_dic2]].append(net_addr)
        except:
            self.node_to_network[self.nodes_dic[network_dic2]] = []
            self.node_to_network[self.nodes_dic[network_dic2]].append(net_addr)

    def add_network(self, net_addr, network_dic1, network_dic2):
        self.network_dic[net_addr] = (network_dic1, network_dic2)

    def add_edge(self, network_dic1, network_dic2):
        self.graph.append([self.nodes_dic[network_dic1], self.nodes_dic[network_dic2]])
        self.graph.append([self.nodes_dic[network_dic2], self.nodes_dic[network_dic1]])

    def get_distances_from_network(self, net_selected):
        network_dic1, network_dic2 = self.get_network_adjs(net_selected)
        ls1 = self.bellman_ford(network_dic1)
        ls2 = self.bellman_ford(network_dic2)
        final_adj = []
        for i in range(self.V):
            final_adj.append(min(ls1[i], ls2[i]))
        return final_adj

    def port_distance_from_network(self, net, nd):
        adj_nets = self.node_to_network[nd]
        adj_routers = []
        for nt in adj_nets:
            network_dic1, network_dic2 = self.network_dic[nt]
            network_node_dic1 = self.nodes_dic[network_dic1]
            network_node_dic2 = self.nodes_dic[network_dic2]
            if network_node_dic1 not in adj_routers and network_node_dic1 != nd:
                adj_routers.append(network_node_dic1)
            if network_node_dic2 not in adj_routers and network_node_dic2 != nd:
                adj_routers.append(network_node_dic2)
        li = self.get_distances_from_network(net)
        minimum = float("Inf")
        selected_router = None
        for i in range(0, len(li)):
            if i in adj_routers and minimum > li[i]:
                minimum = li[i]
                selected_router = i
        intersection_network = set(self.node_to_network[selected_router]) & set(self.node_to_network[nd])

        return 1 + minimum, self.network_ports[nd, intersection_network.pop()]

    def get_distances_from_node(self, router_name):
        node_selected = self.nodes_dic[router_name]
        final_list = []
        nets = self.get_network_dic().keys()
        for net in nets:
            adj_nets = self.node_to_network[node_selected]
            if net in adj_nets:
                final_list.append([net, (0, self.network_ports[node_selected, net])])
            else:
                final_list.append([net, self.port_distance_from_network(net, node_selected)])
        return final_list

    def print_arr(self, dist, node_to_router_dic):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(node_to_router_dic[i], dist[i]))

    def call_bellman_ford(self):
        ticker = threading.Event()
        while not ticker.wait(self.refresh_interval):
            g.bellman_ford(0)

    def bellman_ford(self, src):

        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v in self.graph:
                if dist[u] != float("Inf") and dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1

        return dist


def print_separator():
    print("----------------------------")


print("Enter the Refresh Interval:")
ref_interval = input()
print("Enter the graph Size:")
ln = input()
g = Graph(int(ln), int(ref_interval))
nodes = []
node_to_router_dic = {}

print("Default Names(R0, R1, ..., R(n-1))?[Y/n]")
default_names = input()
if default_names == "Y" or default_names == "y" or default_names == "Yes" or default_names == "":
    for i in range(int(ln)):
        val = "R" + str(i)
        nodes.append(val)
        g.add_node_to_dic(val, i)
        node_to_router_dic[i] = val
else:
    print("Enter the values then:")
    for i in range(int(ln)):
        print(str(i) + ":", end="")
        val = input()
        nodes.append(val)
        g.add_node_to_dic(val, i)
        node_to_router_dic[i] = val

print("names: " + str(nodes))
print(g.get_nodes_dic())
print_separator()
print("Networks Count:", end="")
net_len = input()
print("Enter the graph topology in the following format:\nNode1 Node2 PN1 PN2 (XXX.XXX.XXX.XXX)\n")
for i in range(0, int(net_len)):
    print("{count}:".format(count=i + 1), end="")
    edge = input()
    network_dic1, network_dic2, pn1, pn2, net_addr = edge.split(' ')
    g.add_network_node_port((g.nodes_dic[network_dic1], net_addr), int(pn1))
    g.add_network_node_port((g.nodes_dic[network_dic2], net_addr), int(pn2))
    g.add_edge(network_dic1, network_dic2)
    g.add_network(net_addr, network_dic1, network_dic2)
    g.add_node(net_addr, network_dic1, network_dic2)

t2 = Thread(target=g.call_bellman_ford)
t2.setDaemon(True)
t2.start()

action = ["quit", "add", "report", "change interval", "report router"]
while True:
    print_separator()
    print("Take one of the actions below:")
    print(action)
    print_separator()
    mode = input()
    try:
        if mode == action[0]:
            break
        elif mode == action[1]:
            edge = input()    
            network_dic1, network_dic2, pn1, pn2, net_addr = edge.split(' ')
            g.add_network_node_port((g.nodes_dic[network_dic1], net_addr), int(pn1))
            g.add_network_node_port((g.nodes_dic[network_dic2], net_addr), int(pn2))
            g.add_edge(network_dic1, network_dic2)
            g.add_network(net_addr, network_dic1, network_dic2)
            g.add_node(net_addr, network_dic1, network_dic2)
        elif mode == action[2]:
            i = 0
            NK = g.get_network_dic().keys()
            for item in NK:
                print(str(i) + ":" + item)
                i += 1
            print("Pick a Network from above.\n>>", end="")
            try:
                net_selected = input()
                # The exact same network
                g.print_arr(g.get_distances_from_network(net_selected), node_to_router_dic)
            # g.print_arr(g.get_distances_from(net_selected))
            except:
                print("Couldn't investigate that network")
        elif mode == action[3]:
            g.refresh_interval = int(input())
        elif mode == action[4]:
            i = 0
            RK = g.get_nodes_dic().keys()
            for item in RK:
                print(str(i) + ":" + item)
                i += 1
            print("Pick a Router from above.\n>>", end="")
            try:
                router_selected = input()
                print("[Network Name, (distance, port)]")
                print(g.get_distances_from_node(router_selected))
            except:
                print("Couldn't investigate that Router")

        else:
            print("Action Not Valid!")
    except:
        print("Action is Not Valid")
