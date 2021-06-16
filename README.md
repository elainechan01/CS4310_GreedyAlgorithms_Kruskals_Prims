# Comparison Of Greedy Algorithms (Kruskal's vs Prim's) by Fatima and Elaine

## Project Description

To compare the efficiency between Kruskal’s algorithm using min-heap and the union-find disjoint set data structure and Prim’s algorithm. To compare the efficiency between Prim’s algorithm using adjacency list and binary heap with Prim’s algorithm using adjacency list and fibonacci heap. The main language to be used is Python.

## Project Goals

We are going to create a program that will compare the efficiency between Kruskal’s and Prim’s algorithm by - finding the minimum cost spanning tree between major cities. By theory, Prim's algorithm is more efficient for denser graphs.

Theoretically, these are the following run-times of the two algorithms:
* Prim’s algorithm has a time complexity of (binary heap and adjacency list):
  ```
  O(( |V| +|E|) log |V|) = O(|E| log |V|) 
  ```
  and (Fibonacci heap and adjacency list):
  ```
  O(|E| + |V| log |V|).
  ```
* Kruskal’s algorithm has a time complexity:
  ```
  O(E log E) = O(E log V)

  ```
To efficiently compare the two algorithms, we will implement the algorithms on different types of graphs: one of which is denser. From there, we will implement a detailed timing analysis to compare the efficiency between the execution of algorithms (By running the algorithms 10 times and finding its average runtime). 

Furthermore, we will also implement a comparison between Prim’s algorithm using binary heap and adjacency list with Prim’s algorithm using fibonacci heap and adjacency list. By theory, Prim's algorithm using Fibonacci heap is more efficient on denser graphs.
```
Average runtime = total runtime of 10 loops / 10
```

Theoretically, these are the following run-times between the two versions of Prim’s algorithm:
* Prim’s algorithm has a time complexity of (binary heap and adjacency list) 
 ```
 O(( |V| +|E|) log |V|) = O(|E| log |V|) .
 ```
* Prim’s algorithm has a time complexity of (Fibonacci heap and adjacency list) 
  ```
  O(|E| + |V| log |V|).
  ```
  
To efficiently compare the two algorithms, we will implement the algorithms on different types of graphs: one of which is denser. From there, we will implement a detailed timing analysis to compare the efficiency between the different methods of execution of Prim’s algorithim (By running the algorithms 10 times and finding its average runtime, as well as getting the percentage in runtime).
1.
```
Average runtime = total runtime of 10 loops / 10
```

2.
```
Improvement Percentage = (average runtime of fibonacci heap - average runtime of binary heap) * 100
```

### User Guide

1. Unzip compressed folder, and compile at your preferred IDE (The IDE/Text Editor that we’ve used are: PyCharm Community Edition 2020.1)
2. Open and run “main.py”
3. Enter the filename for the sparse graph, if error is found, re-enter filename. (File should be in “.csv” format, has a header, and its dataset is entered in this format: <Year>;<Source>;<Destination>;<Distance>)
4. Calculations are shown
   - Runtime for Kruskal’s algorithm
   - Runtime for Prim’s algorithm using binary heap
   - Runtime for Prim’s algorithm using fibonacci heap
   - Comparison between Prim’s algorithm using binary heap and fibonacci heap
5. Enter if you’d like to see the MST formed by the three different algorithms, if error is found, re-enter answer. (Input must be either “y” or “n”)
6. Enter the filename for the dense graph, if error is found, re-enter filename. (File should be in “.csv” format, has a header, and its dataset is entered in this format: <Year>;<Source>;<Destination>;<Distance>)
7. Calculations are shown
   - Runtime for Kruskal’s algorithm
   - Runtime for Prim’s algorithm using binary heap
   - Runtime for Prim’s algorithm using fibonacci heap
   - Comparison between Prim’s algorithm using binary heap and fibonacci heap
8. Enter if you’d like to see the MST formed by the three different algorithms, if error is found, re-enter answer. (Input must be either “y” or “n”)

	
	

