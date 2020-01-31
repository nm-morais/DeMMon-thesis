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
* Not applicable for heterogenous devices (keeps similar in-degree per )

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


- intra zone consistency is achieved by employing a gossip algorithm which consists in selecting another agent at random and exhanging state with it. If agents are within the same zone, they exchange state refering to the MIB of their zone, if agents are in different zones, they exchange information related to their least common ancestor in the tree.










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
