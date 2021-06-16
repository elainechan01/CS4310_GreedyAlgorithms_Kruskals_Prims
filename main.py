# import statements here
from math import inf
from os import path
from kruskal import Graph
import prim

import timeit
import csv

"""
Description: to read data from csv file to construct sparse / dense dataset
"""
def read_csv(file_path):
    if not path.exists(file_path):
        return 1, []
    
    rows = []
    file = open(file_path)
    temp = csv.reader(file, delimiter=';')
    for row in temp:
        try:
            toDetermineIndexError = [row[3], row[2], row[1]]
            rows.append(toDetermineIndexError)
        except IndexError:
            return 2, []

    return 0, rows


def run_and_print(g, inFile, is_dense):
    error_code, rows = read_csv(inFile)

    if error_code == 0:
        prims_rows = []
        for row in rows:
            prims_rows.append([row[2], row[1], row[0]])
        g.compute_and_display()
        prim.compute_and_display(prims_rows, is_dense)

def run_algo(is_dense):
    while True:
        inFile = input("Enter file name for {} Graph: ".format('Dense' if is_dense else 'Sparse'))
        error_code, rows = read_csv(inFile)
        if error_code == 1:  # FilenotFound Error
            print("---------------")
            print("File not found")
            print("---------------")
        elif error_code == 2:  #Index Error
            print("-----------------------------------------------------------------------------------")
            print("Error reading file")
            print("Ensure that file contains a header and that the dataset is in the following order: ")
            print("<Year>;<Source>;<Destination>;<Distance>")
            print("------------------------------------------------------------------------------------")
        else:
            iters = 10
            prims_rows = []
            kruskals_rows = []
            for row in rows[1:]:
                prims_rows.append([row[2], row[1], row[0]])
                kruskals_rows.append([float(row[0]), row[1], row[2]])
            g = Graph(kruskals_rows, is_dense=is_dense)
            runtime = timeit.timeit(lambda: g.kruskals(), number=iters)
            print('({} graph) Kruskal\'s using min-heap and union-find disjoint data structure -'.format(
                'Dense' if is_dense else 'Sparse'), runtime, 'seconds')
            prim.compute(prims_rows, is_dense)
            return g, inFile
            break



def main():
    g, infile =run_algo(False) # code to output the runtime for Sparse graph for both the algorithms
    print()
    while True:
        seeMST = input("Would you like to see the MST formed? (y/n) ")
        if seeMST == "y":
            run_and_print(g, infile, False)   #( MST for sparse graph using prims algorithm)
            break
        elif seeMST == "n":
            break
        else:
            print("Invalid input.")
    print()
    g, infile = run_algo(True) # code to output the runtime for Dense graph for both the algorithms
    print()
    while True:
        seeMST = input("Would you like to see the MST formed? (y/n) ")
        if seeMST == "y":
            run_and_print(g, infile, True)  # ( MST for dense graph using prims algorithm)
            break
        elif seeMST == "n":
            break
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
