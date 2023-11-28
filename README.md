# Fast-Dijkstra
The script defines a function dijkstra_n_shortest_paths that efficiently computes a specified number of shortest paths in a weighted graph using Dijkstra's algorithm, returning the paths as an array of tuples.

The provided Python code implements Dijkstra's algorithm to find a specified number of shortest paths (neighborhoods) in a weighted graph starting from a given source node. The algorithm maintains a priority queue to efficiently explore nodes in increasing order of their tentative distances from the source, stopping the search when the specified number of neighborhoods (n_neigh) has been reached. The result is an array of tuples representing paths, each containing the source node, the current node, and the distance of the path.
