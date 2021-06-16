
import math
import random
from time import time

class BinHeap():
    def __init__(self):
        self.A = []
        self.heap_size = 0

    def is_empty(self):
        return self.heap_size == 0

    def swap(self, i, j):
        _ = self.A[i]
        self.A[i] = self.A[j]
        self.A[j] = _

    def parent(self, index):
        return (index - 1) // 2 if index > 0 else None

    def left(self, index):
        index = (index << 1) + 1
        return index if index < self.heap_size else None

    def right(self, index):
        index = (index + 1) << 1
        return index if index < self.heap_size else None

    def min_heapify(self, index):
        l = self.left(index)
        r = self.right(index)

        smallest = l if l is not None and self.A[l] < self.A[index] else index
        smallest = r if r is not None and self.A[r] < self.A[smallest] else smallest

        if smallest != index:
            self.swap(index, smallest)
            self.min_heapify(smallest)

    def heap_min(self):
        return self.A[0] if self.heap_size > 0 else None

    def extract_min(self):
        if self.heap_size == 0:
            return None

        min_val = self.A[0]
        if self.heap_size > 1:
            pop = self.A.pop()
            self.heap_size -= 1
            self.A[0] = pop
            self.min_heapify(0)
        else:
            self.A = []
            self.heap_size = 0

        return min_val

    def decrease_key(self, index, key):
        previous_key, value = self.A[index]
        self.A[index] = (key, value)
        
        while index > 0 and self.A[self.parent(index)] > self.A[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def insert(self, value, key):
        self.heap_size += 1
        self.A.append((key, value))
        self.decrease_key(self.heap_size - 1, key)

class FibNode():
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.children = []
        self.order = 0

    def append(self, t):
        self.children.append(t)
        self.order = self.order + 1

class FibHeap():
    def __init__(self):
        self.nodes = []
        self.least = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def insert(self, value, key):
        new_tree = FibNode(value, key)
        self.nodes.append(new_tree)
        if (self.least is None or key < self.least.key):
            self.least = new_tree
        self.count = self.count + 1

    def get_min(self):
        if self.least is None:
            return None
        return self.least.key, self.least.value

    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for children in smallest.children:
                self.nodes.append(children)
            self.nodes.remove(smallest)
            if self.nodes == []:
                self.least = None
            else:
                self.least = self.nodes[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.key, smallest.value

    def consolidate(self):
        aux = (floor_log(self.count) + 1) * [None]

        while self.nodes != []:
            x = self.nodes[0]
            order = x.order
            self.nodes.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.key > y.key:
                    x, y = y, x
                x.append(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.nodes.append(k)
                if (self.least is None
                        or k.key < self.least.key):
                    self.least = k

def floor_log(x):
    return math.frexp(x)[1] - 1

class Graph():
    def __init__(self, is_dense=True):
        self.adj_list = {}
        self.distance = []
        self.cities = {}
        self.V = 20 if is_dense else 5
        for i in range(self.V):
            self.distance.append([0.0] * self.V)

    def build_graph(self, rows):
        city_index = 0
        for i in range(self.V):
            d = rows[i * 23: (i + 1) * 23]
            d.sort(key=lambda x:x[1])
            d = d[0:self.V]
            
            for _ in d:
                from_city = _[0]
                to_city = _[1]
                dist = float(_[2])

                if from_city != to_city:
                    if from_city not in self.cities:
                        self.cities[from_city] = city_index
                        city_index += 1

                    if to_city not in self.cities:
                        self.cities[to_city] = city_index
                        city_index += 1

                    if from_city not in self.adj_list:
                        self.adj_list[from_city] = []
                    self.adj_list[from_city].append(to_city)

                    if to_city not in self.adj_list:
                        self.adj_list[to_city] = []
                    self.adj_list[to_city].append(from_city)

                    self.distance[self.cities[from_city]][self.cities[to_city]] = dist
                    self.distance[self.cities[to_city]][self.cities[from_city]] = dist
                else:
                    break

    def prims(self, start_city, heap_type):
        mst = set()
        pq = BinHeap() if heap_type == 'b' else FibHeap()
        mst_set = [False] * self.V

        start_city_index = self.cities[start_city]
        mst_set[start_city_index] = True
        cost = 0.0

        t1 = time()
        for node in self.adj_list[start_city]:
            pq.insert((start_city, node), self.distance[start_city_index][self.cities[node]])

        while not pq.is_empty():
            w, cities = pq.extract_min()
            city, u = cities
            index_u = self.cities[u]
            if not mst_set[index_u]:
                cost += w
                mst.add((w, city, u))
                mst_set[index_u] = True
                for v in self.adj_list[u]:
                    if not mst_set[self.cities[v]]:
                        pq.insert((u, v), self.distance[index_u][self.cities[v]])

        self.time = time() - t1
        return mst, cost

    def calc_time(self, heap_type):
        self.time = 0.0
        city = list(self.cities)[random.randint(0, self.V - 1)]
        mst, cost = self.prims(city, heap_type)
        return mst, cost

    def print_graph(self):
        print('Cities are :-')
        for city in self.cities:
            print(city, '-', self.cities[city])

        print()
        print('Adjacency List :-')
        for city in self.adj_list:
            print(city, '-', end='')
            for to_city in self.adj_list[city]:
                print(to_city, '(', self.distance[self.cities[city]][self.cities[to_city]], ')', end=' ')
            print()


def compute_and_display(rows, is_dense):
    dg = Graph(is_dense=is_dense)
    dg.build_graph(rows)

    mst, cost = dg.calc_time('b')
    print('Prims using Binary Heap')
    for edge in mst:
        c, from_city, to_city = edge
        print('Edge: FROM -', from_city, 'TO', to_city, '(Cost: {})'.format(c))
    print('Total cost:', cost)

    mst, cost = dg.calc_time('f')
    print('Prims using Fibonacci Heap')
    for edge in mst:
        c, from_city, to_city = edge
        print('Edge: FROM -', from_city, 'TO', to_city, '(Cost: {})'.format(c))
    print('Total cost:', cost)


def compute(rows, is_dense):
    dg = Graph(is_dense=is_dense)
    dg.build_graph(rows)

    iters = 10

    time_bin = 0.0
    for i in range(iters):
        dg.calc_time('b')
        time_bin += dg.time
    time_bin /= iters

    time_fib = 0.0
    for i in range(iters):
        dg.calc_time('f')
        time_fib += dg.time
    time_fib /= iters

    print('({} graph) Prim\'s using adjacency list and binary heap -'.format('Dense' if is_dense else 'Sparse'), time_bin, 'seconds')
    print('({} graph) Prim\'s using adjacency list and fibonacci heap -'.format('Dense' if is_dense else 'Sparse'), time_fib, 'seconds')
    #print('Improvement -', (abs(time_bin - time_fib) / time_bin) * 100, '%')
    
