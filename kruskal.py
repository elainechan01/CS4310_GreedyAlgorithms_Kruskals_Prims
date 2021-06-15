import csv
import math
import timeit

from heapq import heapify, heappush, heappop

"""
Description: main class to carry out Kruskal's algorithm using min-heap and union-find disjoint data structure
"""
class Graph:
    def __init__(self, arrays, is_dense=True):
        self.V = 20 if is_dense else 5
        self.edges = arrays
        self.MST = []
        self.edgeCount = 0

    def initEdgeList(self):
        self.edgeList = []
        heapify(self.edgeList)
        self.nodesWithRepeat = []
        for i in self.edges:
            heappush(self.edgeList, i)
            self.nodesWithRepeat.append(i[1])
            self.nodesWithRepeat.append(i[2])

    def initDisJointSet(self):
        self.nodes = []
        [self.nodes.append(item) for item in self.nodesWithRepeat if item not in self.nodes]
        self.parent = {}
        for item in self.nodes:
            self.parent[item] = item

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2

    def kruskals(self):
        self.initEdgeList()
        self.initDisJointSet()
        while self.edgeCount < self.V - 1 and self.edgeList:
            edge = heappop(self.edgeList)
            x = self.find(edge[1])
            y = self.find(edge[2])
            if x != y:
                self.edgeCount += 1
                self.union(x,y)
                self.MST.append(edge)
        #print(self.MST)

"""
Description: to read data from csv file to construct sparse / dense dataset
"""
def read_csv():
    file = open('distances-between-main-cities-direct-routes-2013-in-kilometers.csv')
    temp = csv.reader(file, delimiter=';')

    rows = []
    count = 0
    for row in temp:
        count += 1
        if count == 1:
            continue
        rows.append([row[1], row[2], row[3]])
        count += 1

    rows.sort(key=lambda x: (x[0], x[1]))
    return rows

"""
Description: main driver function to carry out Kruskal's algorithm using min-heap and union-find disjoint data structure
and its runtime 
"""
def main():
    rows = read_csv()
    g = Graph(rows,is_dense=False)
    iters = 10
    runtime = timeit.timeit(lambda: g.kruskals(), number=iters)
    print('(Sparse graph) Kruskal\'s using min-heap and union-find disjoint data structure -', runtime, 'seconds')
    dense_g = Graph(rows,is_dense=True)
    dense_runtime = timeit.timeit(lambda: dense_g.kruskals(), number=iters)
    print('(Dense graph) Kruskal\'s using min-heap and union-find disjoint data structure -', dense_runtime, 'seconds')

if __name__ == "__main__":
    main()