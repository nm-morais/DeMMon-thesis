import os
import random
import math
import networkx as nx
import matplotlib.pyplot as plt

NUM_BITS = 128
NUM_NODES = 10
TO_IGNORE_BOUND = 0 

class Node(object):
	"""docstring for Node"""
	def __init__(self, i, nodeId, ignoredBytes):
		super(Node, self).__init__()
		self.i = i
		self.nodeId = nodeId
		self.ignoredBytes = ignoredBytes

def drawNetworkGraph():
	# Need to create a layout when doing
	# separate calls to draw nodes and edgess
	pos = nx.circular_layout(G)
	edge_labels=dict([((u,v,), "{:.2E}".format(d['weight'])) for u,v,d in G.edges(data=True)])
	edges , weights = zip(*nx.get_edge_attributes(G,'weight').items())
	min_w = min(weights)
	max_w = max(weights)
	weights = [weight / (2**128) for weight in weights]
	print(weights)
	node_size= [10 * (128 - node.bit_length()) * 1.0 for node in G.nodes()]
	print(weights)

	#nx.draw_networkx_labels(G, pos, labels, size=3)
	nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=node_size)
	nx.draw_networkx_edges(G, pos, edge_color=weights, edge_cmap=plt.get_cmap("viridis"), arrows=True)
	print(random.random())
	#nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,  font_size=5, alpha=0.5, label_pos=random.random())

	plt.show()



def computeDistance(a, b):
	diff = a.bit_length() - b.bit_length()

	if diff == 0:
		return int(bin(a ^ b), 2)
	elif diff > 0:
		return int(bin((a >> diff) ^ b), 2)
	else:
		return int(bin(a ^ (b >> abs(diff))), 2)

nodeIds = []
labels = {}
G=nx.DiGraph(directed=True)
edge_counter = 0


for i in range(NUM_NODES):
	bytesToIgnore = random.randint(0, TO_IGNORE_BOUND)	
	nodeId = random.getrandbits(NUM_BITS - bytesToIgnore)
	nodeIds.append(Node(i,nodeId, bytesToIgnore))
	labels[nodeId] = bytesToIgnore
	G.add_node(nodeId)
	
for i in nodeIds:

	distances = []
	for j in nodeIds:
		if i != j:
			dist = computeDistance(i.nodeId, j.nodeId)
			distances.append({"nodeId" : j.nodeId, "dist" : dist , "discarded" : j.ignoredBytes})
			#print("Distance to: " + "{0:b}".format(j.nodeId) + "\t=\t" + str(dist))

	#for node in sorted(distances ,  key=lambda node: node["dist"]):
		#print("Discarded Bytes: " + str(node["discarded"]) +  "\tdistance: " + str(node["dist"]) +" \t NodeId: " + "{0:b}".format(node["nodeId"]))

	buckets = []
	for j in range(400):
		buckets.append([])
		for dist in distances:
			if dist["dist"] > (2 ** j) and dist["dist"] < (2 ** (j + 1)):
				buckets[j].append(dist)

	last_added = 0
	for bucketNr, bucket in enumerate(buckets):
		if(bucket):
			if abs(bucketNr - last_added) > math.log(NUM_NODES):
				for node in bucket:
					edge_counter += 1
					print(node["dist"])
					G.add_edge(i.nodeId, node["nodeId"], weight=node["dist"])
					last_added = bucketNr
					break

			#print(bucketNr, [li["discarded"] for li in bucket])		
		
	#print("Total number of nodes in buckets: " + str(total))
print(edge_counter)
drawNetworkGraph()
