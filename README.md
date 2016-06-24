# Py-Graph
[![Build Status](https://travis-ci.org/robertweber95/py-graph.svg?branch=master)](https://travis-ci.org/robertweber95/py-graph)

python implementation of a graph api and graph algorithms.

Created as a study aid for CISC320: Intro to Algorithms

## graph.py
This file contains the class definitions and member functions for a vertex and a graph
#### vertex
+ **key**: an integer label for the vertex
+ **adjacent**: a list of nodes adjacent to this vertex
+ **`addNeighbor(neighbor, [weight=0])`**: method that adds the given vertex to the list of adjacent vertices. The `weight` parameter specifies the weight of the edge between the current vertex and the adjacent vertex.
  + The weight parameter is optional. *If no 2nd value is passed as a parameter, the default weight is 0.*

#### graph
+ **vertList**: List of vertices in the graph.
+ **degrees**: List of the degrees of each vertex in the graph.
+ **numVertices**: Total number of vertices in the graph.
+ **numEdges**: Total number of edges in the graph.
+ **directed**: Boolean that keeps track of whether the graph is directed or not
  + This is an optional parameter of the constructor. *The default value when no value is passed into the constructor is `False`.*
+ **entry**: List of the entry times for each vertex during the DFS
+ **exit**: List of the exit times for each vertex during the DFS
+ **discovered**: List of the discovered states of each node, used during searches.
+ **processed**: List of the processed states of each node, used during searches.
+ **time**: Global counter used for timekeeping in DFS.
+ **`addVertex(key)`**: Adds a new vertex with the ID number of `key`.
+ **`getVertex(key)`**: Returns the vertex with the specified ID.
+ **`addEdge(source, target, [weight=0])`**: Adds an edge to the graph from the vertex `source` to vertex `target` with a weight of `weight`.
+ **`getVertices()`**: Returns a list of the IDs of vertices in the graph.
+ **`sumDegrees()`**: Returns the sum of degrees of all vertices in the graph. Used to prove the Handshake Lemma.
+ **`printGraph()`**: Prints a nice representation of important information of the graph.
+ **`showHandshakeLemma()`**: Prints both the sum of degrees of vertices in the graph and the value of `2*|E|`. These values are equal by the Handshake Lemma.

#### Global functions
+ **`dfs(g, root)`**: Performs a recursive depth-first search on graph `g` by starting at vertex `root`. This returns a list of the parents of every vertex in the graph.
  + The root vertex has a parent of -1.
  + The entry and exit times of each vertex are also saved into the instance `entry` and `exit` lists for graph `g`. These are useful for certain applications of DFS.
+ **`bfs(g, root)`**: Performs a breadth-first search on graph `g` by starting at vertex `root`. This returns a list of the parents of every vertex in the graph.
  + The root vertex has a parent of -1.
+ **`findShortestPath(g, source, target, [parents])`**: Recursively finds the shortest path between two variables using the `parent` list returned by BFS.
  + ***Note:*** *make sure you perform a BFS right before using this method to ensure that your parents list is up to date.* If you happened to add nodes and edges in between the most recent BFS and finding the shortest path, the results will be inaccurate. 
