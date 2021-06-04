Thesis structure:

# 1 - Introduction

## 1.1 Context

- Cloud is the de-facto paradigm -> easy to use, many tools, scalable vertically, simpler algorithms

- however, the bandwith limitations of the cloud infrastracture, and the increasing growth of mobile and Internet of Things applications, coupled with higher demands regarding quality of service and proximity to the end-user, pushed computation outside of the Data-Center to the edge of the network.

- Moving to the edge enables the use of far higher computation power, as there are many more devices in the edge when compared to those found in DCs, however, new bottlenecks arise when making use of such hardware, due to the constrained bandwidth and computing power.

Consequently, it is necessary to coordinate said devices in a way which circumvents their own limitations, and enable the offloading of computation from data-centers to edge devices. This coordination (or control), can be done either in a centralized manner in data-centers, or in a decentralized manner among all nodes integrating the system.

- We believe that because in a centralized scenario, there is the need to carry the necessary information to the same entity, even if said entity is located in a cloud environment, it will become a bottleneck in the system due to bandwidth limitations, making the decentralized control distributed among all nodes the more scalable and fault-tolerant option.

## 1.2 Problem Statement

- Given the aforementioned reasons, there is the need for tools which enable a decentralized control over large numbers of nodes, these must be suited for scenarios with hardware-constrained nodes and high volumes of nodes entering and leaving the system (a phenomena also known as churn). Preferably, said tools must not require manual configuration or rely on a central entity to control the system.

- In this category, there are few tools which strive to do so in a decentralized fashion, and even fewer are those which we believe address the main limitation of performing management of large numbers of nodes in a decentralized manner, which is acquiring, storing, and managing information produced by applications and nodes composing the network.

- This information may be, but is not limited to, the execution of the nodes themselves, but also owned resources (i.e. a graphics card, a replica of a file, or a running service). The main focus of this dissertaion was to create a framework which exposes an API to ease the collection, processing, and creation of alerts to act on this information in a distributed fashion.

## 1.3 Contributions

- The main contributions presented in this thesis are com

- The contributions which arose during the development
