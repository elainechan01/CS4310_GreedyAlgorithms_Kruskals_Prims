import csv

# import statements here
from heapq import heapify, heappush, heappop

"""
Description: main class to carry out Kruskal's algorithm using min-heap and union-find disjoint data structure
"""
class Graph:
    def __init__(self, arrays, is_dense=True):
        """
        :param arrays: dataset containing the undirected graph to calculate the MST
        :param is_dense: if the dataset to be taken into consideration is dense, it contains 20 edges, else 5
        """
        self.V = 20 if is_dense else 5
        self.edges = arrays
        self.MST = []                   # array to store MST
        self.edgeCount = 0              # to store the edge count of the MST

    def initEdgeList(self):
        self.edgeList = []              # create heap to store edges
        heapify(self.edgeList)
        self.nodesWithRepeat = []
        for i in self.edges:
            heappush(self.edgeList, i)
            self.nodesWithRepeat.append(i[1])
            self.nodesWithRepeat.append(i[2])

    def initDisJointSet(self):
        self.nodes = []                 # create list to identify each node/vertice in dataset
        [self.nodes.append(item) for item in self.nodesWithRepeat if item not in self.nodes]
        self.parent = {}                # create dict to store node/vertice of dataset, including its pairing
        for item in self.nodes:
            self.parent[item] = item

    def find(self, item):               # use recursion to find root of item in the appropriate subtree
        if self.parent[item] == item:
            return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res

    def union(self, set1, set2):        # apply union-find disjoint data structure and assign parent pairing
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2

    def kruskals(self):
        self.initEdgeList()             # initialize min-heap
        self.initDisJointSet()          # initialize union-find disjoint data structure
        while self.edgeCount < self.V - 1 and self.edgeList:
            edge = heappop(self.edgeList)       # delete edge with lowest cost from heap
            x = self.find(edge[1])
            y = self.find(edge[2])
            if x != y:                          # if edge does not create a cycle in T (belong to different subtrees)
                self.edgeCount += 1
                self.union(x,y)                 # join (union) the subtrees of x and y
                self.MST.append(edge)
