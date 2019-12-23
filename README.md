

# \<Undefined Project Name\> - 
## MSc Thesis for Nuno Morais (student nr 49544)

### 1. Project Objective

The goal of this project is to (hopefully)  develop a new innovative algorithm for peer-to-peer networks 
which takes into account device heterogeneity and builds a topology that can efficiently be used for 
aggregating values / monitoring edge devices.

This information can then be leveraged upon to be able to deploy services (e.g. in areas where there are hotspots of user activity), monitor service health, monitor device status. (macro view)

### 2. Objectives to tackle


1. Building an efficient topology for a network of massive scale  (leveraging on gossip) (Hierarchy is the first idea)

2. Aggregate information in order to improve the topology and deploy services 

3. Figure out how to reliably transfer / maintain microservices on edge devices

4. Query over this topology for efficient deployment


### 3. Ideas

1. Leverage on cloud computing to calculate the best possible configuration of the network

2. Use Edge Data centers as super peers for extending computation to client devices.

3. Build a network composed of many levels e.g. (Ranked based on network and computation capabilities):

     Leverage on 2 types of groups to maintain / optimize topology:

    * Vertical Groups - used membership and service deployment
    * Horizontal Groups  - used for aggregation

    Together these form a topology similar to a FAT-tree

4. many ideas were had but forgotten

### 4. TODOS

1. Research lots more
2. Find efficient simulator for edge networks / build a new one
3. Pass notes from paper to digital