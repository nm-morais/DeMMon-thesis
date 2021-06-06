Thesis structure:

# 1 - Introduction

## 1.1 Context

- Cloud is the de-facto paradigm -> easy to use, many tools, scalable vertically, simpler algorithms

- however, the bandwith limitations of the cloud infrastracture, and the increasing growth of mobile and Internet of Things applications, coupled with higher demands regarding quality of service and proximity to the end-user, pushed computation outside of the Data-Center to the edge of the network.

- Moving to the edge enables the use of far higher computation power, as there are many more devices in the edge when compared to those found in DCs, however, new bottlenecks arise when making use of such hardware, due to the constrained bandwidth and computing power.

Consequently, it is necessary to coordinate said devices in a way which circumvents their own limitations, and enable the offloading of computation from data-centers to edge devices. This coordination (or control), can be done either in a centralized manner in data-centers, or in a decentralized manner among all nodes integrating the system.

- falar de edge-enabled applications

- We believe that because in a centralized scenario, there is the need to carry the necessary information to the same entity, even if said entity is located in a cloud environment and has the ability to vertically scale. Conseqeuntly, in addition to being a sole point of failure of the system, it will eventually become a bottleneck due to bandwidth limitations, making the decentralized control distributed among all nodes the more scalable and fault-tolerant option.

## 1.2 Problem Statement

- Given the aforementioned reasons, there is the need for tools which enable a decentralized control over large numbers of nodes, these must be suited for scenarios with hardware-constrained nodes and high volumes of nodes entering and leaving the system (a phenomena also known as churn), and preferably, said tools must not require manual configuration.

- In this category, there are few tools which strive to do so in a decentralized fashion, and even fewer are those which address the main limitation of performing management of large numbers of nodes in a decentralized manner, which is require, storing and managing information produced by applications and nodes composing the network.

- This information may be, for example, related to the execution of devices, or about owned resources (i.e. a graphics card, a replica of a file, or a running service), the main focus of this dissertation is to attempt to ease solving this problem by creating a distributed information management framework, which provides an API to ease the collection, processing, and dissemination of information, targeted for decentralized service management systems.

- Following, we have a picture ilustrating an overview of the idealized structure of the previosuly mentioned idea, where in the bottom there is a network management layer, which creates optimized logical connections ammong nodes used to propagate information. Using that layer, a monitoring layer employs the established connections to collect and aggregate information, and lastly, a control layer, which in turn uses the monitoring information to perform actions (e.g. optimizing deployment of services).

|----------------------------|
| edge-enabled Applications |
|----------------------------|
| Control layer |
|----------------------------|
| Monitoring layer |
|----------------------------|
| Network layer |
|----------------------------|

## 1.3 Contributions

- The main contributions of this dissertation focus on creating the monitoring and networking layer, as illustrated in the picture:

- For the networking layer, the main contributions consist of an overlay protocol which strives to build a logical tree using both bandwidth, latency, and other mechanisms to improve node proximity. To create this overlay network, a framework (GO-BABEL) similar to BABEL was created. While the execution model is the exact same as BABEL, GO-BABEL has some additions to ease the collection of latency, and detect failures.

- Regarding the monitoring layer, a distribured monitoring protocol was built, which uses the connections created by the overlay protocol, and the tree structure to perform efficient aggregations. These aggregations are performed on-demand, and based on commands issued by the API.

- In addition to these two main contributions, in order to test the full-fleged system, a benchmark for an edge-enabled application was created in collaboration with a colleague to test the infrastructure described in pic X, this benchmark is composed by multiple loosely coupled micro-services, and a client for those microservices, where geographical proximity leads to a significant improvement of QOS for the end-user.

- Lastly, to test the system and its capalities against known alternatives in the state of the art, multiple benchmarks were devised:

  - a membership benchmark, where the membership protocol's fault tolerance and ability to improve the network is tested against popular membership protocols in the state of the art. The implemented protocols are: Hyparview, X-BOT, Cyclon and T-Man with Cyclon as its source for initial view.

  - A broadcast benchmark, which used the implemented membership protocols and uses both a simple flood mechanism, and an implementation of PlumTree, to test the protocol's throughput, ability to perform information dissemination reliably, and fault tolerance.

  - A monitoring benchmark, this benchmark evaluates the designed monitoring layer against common prometheus configurations. In this benchmark, the accuracy of the collected monitoring values is collected over time, along with information regarding the networking and processing power used to collect the information.

## 1.4 Document Organization

# 2 Related work

## 2.1 Cloud and edge computing

- falar sobre porque é que a cloud se instaurou, os problemas que advém e porque e que estamos a mexer-nos para a edge

### 2.1.1 Other computing paradigms

- falar de outros paradigmas semelhantes, como o osmotic computing, fog computing, e outros que encontre, falar de como são semelhantes, mas a nossa
  versao esta focada no uso da infrastrutura

## 2.2 Overlay networks

### 2.2.1 Unstructured and structured overlays

### 2.2.2 Properties of overlay networks

### 2.2.3 Tools to build overlay networks

### 2.2.4 Related overlay networks

### 2.2.4 Summary

## 2.3 Monitoring solutions

### 2.3.1 Properties of monitoring solutions

### 2.3.1 Related monitoring solutions

### 2.3.3 Conclusion

# 3 The DeMMon framework

## 3.1 GO-Babel framework

### 3.3.1 Design choices

## 3.2 Overlay network

## 3.2 Monitoring protocol

## 3.3 DeMMon API

## 3.3 DeMMon API showcase ??

## 3.3 Summary

# 4 Benchmark

## 4.1 Overview

## 4.2 Design choices

## 4.3 Summary

# 5 Evaluation

## 5.1 Overlay network

## 5.3 Broadcast

## 5.2 Monitoring

## 6 Conclusion and future work
