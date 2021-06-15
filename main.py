# import statements here
from kruskal import read_denseGraph, read_sparseGraph, Graph

import timeit

def main():
    # kruskal's algorithm to read a sparse graph
    rows = read_sparseGraph()
    g = Graph(rows,is_dense=False)
    iters = 10
    runtime = timeit.timeit(lambda: g.kruskals(), number=iters)
    print('(Sparse graph) Kruskal\'s using min-heap and union-find disjoint data structure -', runtime, 'seconds')
    # prim's algorithm to read a sparse graph (fib heap)
    #### to be edited
    # prim's algorithm to read a sparse graph (bin heap)
    #### to be edited

    #kruskal's algorithm to read a dense graph
    rows = read_denseGraph()
    dense_g = Graph(rows,is_dense=True)
    dense_runtime = timeit.timeit(lambda: dense_g.kruskals(), number=iters)
    print('(Dense graph) Kruskal\'s using min-heap and union-find disjoint data structure -', dense_runtime, 'seconds')
    # prim's algorithm to read a dense graph (fib heap)
    #### to be edited
    # prim's algorithm to read a dense graph (bin heap)
    #### to be edited


if __name__ == "__main__":
    main()