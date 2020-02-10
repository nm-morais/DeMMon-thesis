# tese_edge_monitoring
## Researched papers:

## Build One, Get One free

### Description
Combines Joins Pastry with a gossip algorithm that groups clusters of nodes
based on an interest metric. 

Uses formed clusters to selectively fill the routing tables of Pastry.
Then uses Pastry leaf nodes to substitute the random peer sampling service that is 
then employed to form clusters.

### Notes
Really smart, does not improve Routing performamce, but reduces number of
overall messages sent

## Kademlia : 

Peer-to-peer distributed hash table

* Minimizes number of configuration messages nodes must send to learn about each other
* Spreads configuration information in key lookups
* Paralel, assyncronous querying

Uses XOR as a metric for distance between points in key-space (XOR is symmetric)

#### Main differences with other DHT's:

* To locate nodes near a particular ID, uses single routing algorithm from start to finish.
* Similar to pastry in routing, converges to target in log steps. 
  But, in a second phase, Pastry switches to distance metric
  to numeric difference metric between ID, which can create
  discontinuities at particular node ID values, reducing 
  performance and complicating formal analysis of worst case behavior. 
  Kademlia uses as Xor as a metric for distance and circumvents this problem.

#### XOR distance

returns a distance that is directly correlated to the similarities between IDs

Example for two nodes with very distict nodes: 

101 xor 010 = 111 = 8

Closer nodes (larger common prefix in IDS):

110 xor 111 = 001 = 1

Order matters:

1111111111 xor 1111111110 = 0000000001 = 1

1111111111 xor 0111111111 = 1000000000 = 512

#### Node State:

ID composed of 160 bits
For each 0 < i < 160, every node keeps a list of <IP, UDP port,Node ID> 
corresponding to nodes that are distance between 2^i and 2^{i + 1} (k-Buckets)
K-Buckets contain node adresses sorted by last time seen. 
Many K-buckets will be empty (mainly for small values of i)
For large values of i, many K-buckets will fill up until a parameter K
k depends on how many nodes can fail within an hour of each other

 #### How it works:

Piggybacks control messages on requests
Whenever a node receives a message, if the node is already in a 
k-bucket, it will refresh the last time seen,
if it is not in the k-bucket, the recipient checks the state of the
least recently seen node in that bucket by
pinging it. If the node responds, then the receiver does not add the
sender to the bucket, else, it drops the 
failed node and adds the new node to the bucket.

Operations : 4 RPS (PING, STORE; FIND_NODE , FIND_VALUE)
Find_Node returns the k-nodes it knows about closest to the target, which come from the closest k-buckets to the target.
Find_Value behaves like Find_Node but if the recipient has received a Store RPC for the key, it just returns it.
Ping and Store are their intuitive meanings

#### Node Lookup:

Node initiator sends paralel, asynchronous FIND_NODE RPCs to the α closest nodes it knows about. 
α Is a system-wide concurrency parameter

#### JOIN

Join is a node lookup for its own id, 
then the node refreshes all k-buckets further away than its closest neighbour ( Fills routing table)
During this, the entering node populates its own k-bucket and inserts itself into other k-buckets.

#### Notes:

* The longer a node has been up, the more likely it is to remain up for another hour.
* Resistant to certain DOS attacks like flushing nodes from routing tables by flooding system with new nodes.
 This is ensured because nodes prioritize others who have been up longer in their tables.

## Tapestry:

#### Description

Overlay location and routing infrastructure that provides location-independent routing of
messages directly to the closest copy of an object or service using only point-to-point links
and without centralized resources. Slef-administering, fault-tolerant and resilient under load.


#### Routing

Employs a routing  mechanism inspiredi in Plaxton Which incrementaly forwards messages to
the destination ID digit by digit. Uses local routing maps at each node that are called
neighbor maps that incrementally route overlay messages to the destination.

Routes messages to the destination in logb(N) where b is the base of the ID

e.g. ***8 -> **98 -> *598 -> 4598

Every destination node is the root node of its own tree, which is a unique spanning 
tree across all nodes. Any leaf can transverse a number of intermediate nodes en route 
to the root node.

### DECA:

Introduces a Hierarchical methodology based on cayley graphs that produces hierarchical
systems from usual flat DHTs. Then employs an aggregation mechanism that employs gossip
to achieve scalability. 

Pros : Good for locality in DHTS (heavily outperforms chord)

Cons :
* Does not compare with more sophisticated DHTs like Kademlia, Pastry or Tapestry 
* Not applicable for heterogenous devices (keeps similar in-degree per node)

## Mesos:

### Summary

* a platform for sharing commodity clusters between multiple diverse cluster computing frameworks, such as Hadoop and MPI
* Proposes solving fine-grained resource sharing across frameworks
* Uses Zookeeper for fault-tolerance

### Notes

* Facebook uses a 2000 node cluster
* Emulation results w/ 50000 slave daemons on 99 amazon machines, 200 frameworks w/ 20-second tasks, and two mesos masters connected to a 5-node Zookeeper quorum
* Resource offers force a type of programming model on frameworks that may not be desirable
* Uses Linux Containers for isolating CPU usage
* Frameworks can filter proposals by providing pre-established filters.
* Centralized scheduler


### Behavior

* Mesos decices how many resources to offer to each framework, and 
frameworks then decide which resources to accept and which computations to run on them
* Each resource offer consists in a list of free resources on multiple slaves 
* Consists of a master process that manages slave daemons running on each cluster node
 
1. Slave reports to master that has 4 CPUs and 4 GB RAM free
2. Master sends resource offer to framework
3. Framework scheduler replies to master with tasks to execute
4. Master sends tasks to slave, which allocates appropriate resources to framework's executor

### Limitations

* Centralized
* Resource offers limit programming model

## ENORM:

* Framework for deploying partitioned servers on edge nodes
* Uses geographical data relevant to the edge node's location to partition the application (e.g. edge server in Lisbon holds information form users in Lisbon)
* Uses an auto-scaling, amd a mechanism to manage the workload for maximizing the performance of containers that are hosted on the edge by periodically monitoring resource utilization.
* Achieves up to 95% reduction traffic and communication frequency and latency from 20%-80%

## Astrolabe 

- Establishes a tree hierarchy among nodes 
- Each zone has a unique identifier, unique within the parent zone
- Hierarchy is defined by the zones (e.g. USA/Cornel/pc3)
- Information is aggregated up the hierarchy  using aggregation functions
- Each zone has an MIB of child zones which has a summary of their attributes
- Leafs zones of the tree have sets of virtual child zones, which produce a summary of attributes
- aggregation functions which aggregate these MIBs are programmable, and are added to the correspondent MiB with a reserved name, learned by a gossip protocol
- Use cases include: File system, PubSub , Peer-to-peer diffusion and Synchronization

Implementation

- all nodes run an astrolabe agent
- each agent has access to only a subset of all the MIBs in the astrolabe zone tree (all the zones on the path to the root as well as the sibling zones of each of those)
- MIBs from different agents in a zone may be different even if queried at the same time
- Utilizes a probabilistic consistency model


- intra zone consistency is achieved by employing a gossip algorithm which consists in selecting another agent at random and exchanging state with it. If agents are within the same zone, they exchange state refering to the MIB of their zone, if agents are in different zones, they exchange information related to their least common ancestor in the tree.


## Scalable Distributed Information Management System

SDIMS satisfies four properties: scalability, flexibility in API, administrative isolation and robustness to node and network reconfigurations. Inspired in Astrolabe and DHTs

* Administrative isolation : queries about an administrative domain's information can be satisfied within the domain, so the system can operate during disconnections from other domains, so that an external observer cannot monitor or affect intra-domain queries, and to support domain-scoped queries efficiently.

Each data entry is a tuple (attrType, attrName, value), and the system associates aggregation functions with attribute types, and for each level-i subtree in the system, the system defines an aggregate value for each (attrType, attrName).

Makes simple modifications to Pastry routing tables to yield an Autonomous DHT w/ path locality and path convergence. Whenever two nodes in a domain share the same prefix with respect to a key and no node in the domain has a longer prefix, SDIMS introduces a virtual node at the boundary of the domain corresponding to that prefix plus the next digit of the key. This node is simulated by the existing  node whose id is numerically closest to the virtual node's id. (this is weird)

Very strict aggregation rules, load is homogeneous among nodes, reconfigurations are expensive. Does not handle composite queries, because attributes are aggregated along different trees.

Not very applicable to monitoring systems because in a monitoring system all nodes communicate all values, therefore, there will be a short amount of attributes in the system. However, it is interesting as a building block for a cloud system (or a platform which servers as support for edge nodes).







##############################################################################

## OMEGA:

Omega is a scheduler designed for grid computing systems composed by schedulers and workers.
Each scheduler receives large amounts of jobs composed by either one or many tasks that 
have to be scheduled among workers. Contrary to YARN, which is monolithic, OMEGA uses
multiple schedulers per cluster, each with a shared global view of the cluster state.

Schedulers make task placement decisions according to their view of the cluster state and their scheduling policy.
If 2 or more schedulers attempt to schedule a task to the the same worker (conflict), the worker first tries to 
accommodate both tasks, if it cant, it rejects the least important one.

One advantage of OMEGA vs YARN is that YARN resource attributions "lock" the resources to the corresponding framework, 
which means that only one framework is examining a resource at a time, effectively holding a lock on that resource for the duration of a scheduling decision. Limitations from OMEGA are that, in case the grid becomes overloaded,
resource allocations can potentially start interfering with each other, and scheduling policies are harder to ensure.

 ## MON:

Management Overlay Network (MON) is a distributed system aimed
at facilitating the management of large distributed applications.
MON builds on-demand overlay structures that allow users to execute
instant management commands, such as query the current status of the 
application, or push software updates to all the nodes. This means
that MON does not have a cost when there are no commands running.

The on-demand overlay construction allows the creation of two structures: 

 * Tree: a MON client sends a Session message to a nearby MON server, the MON server
    responds with SessionOK, become a child of the session and forward the message to other nodes.
    If a node receives a Session message for the second time, it answers with a Prune message.

  * DAG: modifying the above algorithm by adding assigning levels to nodes, where the root node is level 1
    and the remaining nodes are 1 plus the level of their first parent. If a node receives a second SESSION,
    it can accept the message sender as a secondary parent, which creates a DAG.

The authors then employ the created overlays for aggregating monitoring data related to
the status of the devices by scraping data from the monitoring probe located in each node and aggregating
it up the hierarchy.

One limitation from MON is that the resulting overlays are susceptible to topology mismatch and
do not ensure connectivity. In addition, from the point of view of speeding up resource allocations towards
resource sharing systems, it is preferable for nodes to continuously aggregate data instead of performing 
on-demand aggregations.

## THICKET

Thicket is a protocol which aims at establishing and maintaining multiple broadcast trees over a single unstructured 
overlay network. However, unlike other approaches, thicket tries to make the trees independent from each other, such
that failures affect each tree as little as possible. 

The tree construction is as follows: for each tree, the source node selects a subset of its peers, sends them a message
and establishes an active connection with them, every non-source node that is not already interior in any tree forwards the 
message to other peers and becomes an interior node. Nodes that are already interior in a tree stop the branching process and
become a leaf in the tree.

This however does not ensure that all nodes belong to all trees, to ensure this, Thicket applies a tree repair
which relies on nodes periodically exchanging a SUMMARY message containing all identifiers of fresh messages received and the local forwarding load. If a node receives a SUMMARY message and detects that it has not received a message, it sets up a tree repair timer associated to that message. 

Whenever the repair timer triggers and the corresponding message has not been received in the meanwhile,
the node which detected the fault in the tree attempts to chose another node to replace the failed tree
from the pool of nodes from which it received the SUMMARY message containing the missing message. 
The selection is made based on the forwarding load of each node, where the selected node can reject being selected.

Thicket effectively builds an overlay where almost 100% of nodes are interior in a single spanning tree, significantly 
improving load balancing properties in tree-based multicast systems, as long as each tree is used to transmit similar amounts of data. Limitations of thicket are: (1)  assumes that source nodes and nodes that serve as root nodes never fail; (2) the load balancing properties of the overlay do not take into account device heterogeneity nor network congestion; (3) the number of connections is linear with respect with the number of trees (4) the trees may become unbalanced as a function of the underlying network.

## FogTorch

FogTorch is a service deployment framework aimed at determining eligible 
deployments of an application over a given Fog infrastructure. The authors 
model the fog infrastructure, IoT applications and eligible deployments considering
IoT devices and QoS constraints.

### System Model:

The authors model the Fog infrastructure as follows:

* Cloud Data Centers: Cloud DCs are denoted by their location and software capabilities it provides.
* Fog Nodes: A fog node has is a tuple which contains the location, hardware and software capabilities and the things directly reachable from it
* Things: A tuple denoting the thing location and its type
* QoS profiles: A set of QoS profiles consists of a set of pairs composed by the latency and bandwidth of a communication link.
* Applications: which are composed of independent sets of components,
 each with a set of requirements regarding QoS profiles, hardware and software capabilities, and things.

Then, authors model the notion of service deployments as restrictions over the aforementioned system model and
employ a greedy heuristic which reduces the search space of devices that constitute options for service deployments.

FogTorch originated FogTorchPI, which employs the same system model but instead of searching over all possible deployment combinations, it employs Monte Carlo simulations, and returns a set of eligible deployments along with their QoS-assurance, heuristic rank and resource consumptions. FogTorch provides a comprehensive system model which is able to model many different types of application requirements, however, a limitation from the proposed service deployment algorithms is that they require a global up-to-date global view of the system, which would heavily limit system scalability.

## 

### Edge

### Unstructured Overlay Networks

#### Membership

  * HyparView
  * Cyclon
  * X-Bot
  * Overnesia

### Structured Overlay Networks

  * Chord
  * T-Man
  * Scatter
  * Pastry
  * Kelips

### Monitoring systems

  * Ganglia
  * Astrolabe

### Aggregation

  * Gossip-based Aggregation in Large Dynamic Networks

### Other

  * Scribe
  * PlumTree

### need reviewing


## Notes

Mobile-edge computing (Multi-access edge computing) 

- Monitoring

Borg, Omega, Kubernetes
Yarn 
Mesos


### Simulators for edge networks
  * PeerSim
  * INET Framework (https://github.com/inet-framework/inet) / 
  * ModelNet
  * GT-ITM (Topology generator)
  * SIMPSON
  * iFogSim (https://onlinelibrary.wiley.com/doi/full/10.1002/spe.2509)
  * EdgeCloudSim
