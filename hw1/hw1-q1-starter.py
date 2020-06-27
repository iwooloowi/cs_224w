################################################################################
# CS 224W (Fall 2019) - HW1
# Starter code for Question 1
# Last Updated: Sep 25, 2019
################################################################################
import random

import snap
import numpy as np
import matplotlib.pyplot as plt

# Setup
erdosRenyi = None
smallWorld = None
collabNet = None


# Problem 1.1
def genErdosRenyi(N=5242, E=14484):
    """
    :param - N: number of nodes
    :param - E: number of edges

    return type: snap.PUNGraph
    return: Erdos-Renyi graph with N nodes and E edges
    """
    ############################################################################
    # TODO: Your code here!
    Graph = snap.TUNGraph.New(N, E)
    for i in range(N):
        Graph.AddNode(i)

    for i in range(E):
        src_node_id = random.randint(0, N-1)
        result = False
        while not result:
            dst_node_id = random.randint(0, N-1)
            if dst_node_id == src_node_id:
                result = False
            else:
                exist = Graph.IsEdge(src_node_id, dst_node_id)
                if exist:
                    result = False
                else:
                    Graph.AddEdge(src_node_id, dst_node_id)
                    result = True

        # Graph.AddEdge(src_node_id, dst_node_id)
    ############################################################################
    return Graph


def genCircle(N=5242):
    """
    :param - N: number of nodes

    return type: snap.PUNGraph
    return: Circle graph with N nodes and N edges. Imagine the nodes form a
        circle and each node is connected to its two direct neighbors.
    """
    ############################################################################
    # TODO: Your code here!
    E = 2*N + 4000
    Graph = snap.TUNGraph.New(N, E)
    for i in range(N):
        Graph.AddNode(i)

    for i in range(N):
        src_node_id = i
        dst_node_0 = i - 1
        if dst_node_0 < 0:
            dst_node_0 = N + dst_node_0
        dst_node_1 = i + 1
        if dst_node_1 >= N:
            dst_node_1 = dst_node_1 % N

        if not Graph.IsEdge(src_node_id, dst_node_0):
            Graph.AddEdge(src_node_id, dst_node_0)

        if not Graph.IsEdge(src_node_id, dst_node_1):
            Graph.AddEdge(src_node_id, dst_node_1)

    for i in range(N):
        src_node_id = i
        dst_node_0 = i - 2
        if dst_node_0 < 0:
            dst_node_0 = N + dst_node_0
        dst_node_1 = i + 2
        if dst_node_1 >= N:
            dst_node_1 = dst_node_1 % N
        
        if not Graph.IsEdge(src_node_id, dst_node_0):
            Graph.AddEdge(src_node_id, dst_node_0)

        if not Graph.IsEdge(src_node_id, dst_node_1):
            Graph.AddEdge(src_node_id, dst_node_1)

    total_random_connections = 4000
    count_random_connections = 0
    while count_random_connections < total_random_connections:
        src_node_id = random.randint(0, N-1)
        dst_node_id = random.randint(0, N-1)
        if not Graph.IsEdge(src_node_id, dst_node_id):
            Graph.AddEdge(src_node_id, dst_node_id)
            count_random_connections += 1
    ############################################################################
    return Graph


def connectNbrOfNbr(Graph, N=5242):
    """
    :param - Graph: snap.PUNGraph object representing a circle graph on N nodes
    :param - N: number of nodes

    return type: snap.PUNGraph
    return: Graph object with additional N edges added by connecting each node
        to the neighbors of its neighbors
    """
    ############################################################################
    # TODO: Your code here!

    ############################################################################
    return Graph


def connectRandomNodes(Graph, M=4000):
    """
    :param - Graph: snap.PUNGraph object representing an undirected graph
    :param - M: number of edges to be added

    return type: snap.PUNGraph
    return: Graph object with additional M edges added by connecting M randomly
        selected pairs of nodes not already connected.
    """
    ############################################################################
    # TODO: Your code here!

    ############################################################################
    return Graph


def genSmallWorld(N=5242, E=14484):
    """
    :param - N: number of nodes
    :param - E: number of edges

    return type: snap.PUNGraph
    return: Small-World graph with N nodes and E edges
    """
    Graph = genCircle(N)
    Graph = connectNbrOfNbr(Graph, N)
    Graph = connectRandomNodes(Graph, 4000)
    return Graph


def loadCollabNet(path):
    """
    :param - path: path to edge list file

    return type: snap.PUNGraph
    return: Graph loaded from edge list at `path and self edges removed

    Do not forget to remove the self edges!
    """
    ############################################################################
    # TODO: Your code here!
    Graph = None

    ############################################################################
    return Graph


def getDataPointsToPlot(Graph):
    """
    :param - Graph: snap.PUNGraph object representing an undirected graph

    return values:
    X: list of degrees
    Y: list of frequencies: Y[i] = fraction of nodes with degree X[i]
    """
    ############################################################################
    # TODO: Your code here!
    X, Y = [], []

    ############################################################################
    return X, Y


def Q1_1():
    """
    Code for HW1 Q1.1
    """
    global erdosRenyi, smallWorld, collabNet
    erdosRenyi = genErdosRenyi(5242, 14484)
    smallWorld = genSmallWorld(5242, 14484)
    collabNet = loadCollabNet("ca-GrQc.txt")

    x_erdosRenyi, y_erdosRenyi = getDataPointsToPlot(erdosRenyi)
    plt.loglog(x_erdosRenyi, y_erdosRenyi, color = 'y', label = 'Erdos Renyi Network')

    x_smallWorld, y_smallWorld = getDataPointsToPlot(smallWorld)
    plt.loglog(x_smallWorld, y_smallWorld, linestyle = 'dashed', color = 'r', label = 'Small World Network')

    x_collabNet, y_collabNet = getDataPointsToPlot(collabNet)
    plt.loglog(x_collabNet, y_collabNet, linestyle = 'dotted', color = 'b', label = 'Collaboration Network')

    plt.xlabel('Node Degree (log)')
    plt.ylabel('Proportion of Nodes with a Given Degree (log)')
    plt.title('Degree Distribution of Erdos Renyi, Small World, and Collaboration Networks')
    plt.legend()
    plt.show()


# Execute code for Q1.1
Q1_1()


# Problem 1.2 - Clustering Coefficient

def calcClusteringCoefficientSingleNode(Node, Graph):
    """
    :param - Node: node from snap.PUNGraph object. Graph.Nodes() will give an
                   iterable of nodes in a graph
    :param - Graph: snap.PUNGraph object representing an undirected graph

    return type: float
    returns: local clustering coeffient of Node
    """
    ############################################################################
    # TODO: Your code here!
    C = 0.0

    ############################################################################
    return C

def calcClusteringCoefficient(Graph):
    """
    :param - Graph: snap.PUNGraph object representing an undirected graph

    return type: float
    returns: clustering coeffient of Graph
    """
    ############################################################################
    # TODO: Your code here! If you filled out calcClusteringCoefficientSingleNode,
    #       you'll probably want to call it in a loop here
    C = 0.0

    ############################################################################
    return C

def Q1_2():
    """
    Code for Q1.2
    """
    C_erdosRenyi = calcClusteringCoefficient(erdosRenyi)
    C_smallWorld = calcClusteringCoefficient(smallWorld)
    C_collabNet = calcClusteringCoefficient(collabNet)

    print('Clustering Coefficient for Erdos Renyi Network: %f' % C_erdosRenyi)
    print('Clustering Coefficient for Small World Network: %f' % C_smallWorld)
    print('Clustering Coefficient for Collaboration Network: %f' % C_collabNet)


# Execute code for Q1.2
Q1_2()
