# import statements here
from kruskal import read_denseGraph, read_sparseGraph, Graph

import timeit
import csv

def main():
    # get user's input and include error handling
    validInput = False
    while not validInput:
        inFile = input("Enter file name for Sparse Graph: ")
        try:
            infile = open(inFile)
            temp = csv.reader(infile, delimiter=';')
            for row in temp:
                toDetermineIndexError = [row[3], row[2], row[1]]
        except FileNotFoundError:
            print("---------------")
            print("File not found")
            print("---------------")
            validInput = False
        except IndexError:
            print("-----------------------------------------------------------------------------------")
            print("Error reading file")
            print("Ensure that file contains a header and that the dataset is in the following order: ")
            print("<Year>;<Source>;<Destination>;<Distance>")
            print("------------------------------------------------------------------------------------")
            validInput = False
        else:
            # kruskal's algorithm to read a sparse graph
            infile = open(inFile)
            rows = read_sparseGraph(infile)
            g = Graph(rows,is_dense=False)
            iters = 10
            runtime = timeit.timeit(lambda: g.kruskals(), number=iters)
            print('(Sparse graph) Kruskal\'s using min-heap and union-find disjoint data structure -', runtime, 'seconds')
            # prim's algorithm to read a sparse graph (fib heap)
            #### to be edited
            # prim's algorithm to read a sparse graph (bin heap)
            #### to be edited
            infile.close()
            validInput = True
    # get user's input and include error handling
    validInput = False
    while not validInput:
        inFile = input("Enter file name for Dense Graph: ")
        try:
            infile = open(inFile)
            temp = csv.reader(infile, delimiter=';')
            for row in temp:
                toDetermineIndexError = [row[3], row[2], row[1]]
        except FileNotFoundError:
            print("---------------")
            print("File not found")
            print("---------------")
            validInput = False
        except IndexError:
            print("-----------------------------------------------------------------------------------")
            print("Error reading file")
            print("Ensure that file contains a header and that the dataset is in the following order: ")
            print("<Year>;<Source>;<Destination>;<Distance>")
            print("------------------------------------------------------------------------------------")
            validInput = False
        else:
            #kruskal's algorithm to read a dense graph
            rows = read_denseGraph(infile)
            dense_g = Graph(rows,is_dense=True)
            iters = 10
            dense_runtime = timeit.timeit(lambda: dense_g.kruskals(), number=iters)
            print('(Dense graph) Kruskal\'s using min-heap and union-find disjoint data structure -', dense_runtime, 'seconds')
            # prim's algorithm to read a dense graph (fib heap)
            #### to be edited
            # prim's algorithm to read a dense graph (bin heap)
            #### to be edited
            infile.close()
            validInput = True

if __name__ == "__main__":
    main()