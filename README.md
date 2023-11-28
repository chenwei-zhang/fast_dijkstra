# Fast-Dijkstra: Dijkstra's N-Shortest Paths Finder
The script defines a function dijkstra_n_shortest_paths that efficiently computes a specified number of shortest paths in a weighted graph using Dijkstra's algorithm, returning the paths as an array of tuples.

## Overview

The `dijkstra_n_shortest_paths` function is a Python implementation of Dijkstra's algorithm to find a specified number of shortest paths in a weighted graph.

## Installation

```bash
pip install fast-dijkstra
```

## Usage

```python
import numpy as np
from fast_dijkstra import dijkstra_n_shortest_paths

# Define a weighted graph as a dictionary
weighted_graph = {
    'A': {'B': {'weight': 1}, 'C': {'weight': 4}},
    'B': {'A': {'weight': 1}, 'C': {'weight': 2}},
    'C': {'A': {'weight': 4}, 'B': {'weight': 2}},
}

# Find the top 3 shortest paths starting from node 'A'
result_paths = dijkstra_n_shortest_paths(weighted_graph, 'A', n_neigh=3)

print(result_paths)
```

## Function Signature

```python
def dijkstra_n_shortest_paths(graph, source, n_neigh=100):
    """
    Find a specified number of shortest paths in a weighted graph using Dijkstra's algorithm.

    Parameters:
    - graph (dict): The input graph represented as a dictionary.
    - source (hashable): The starting node for the Dijkstra's algorithm.
    - n_neigh (int, optional): The maximum number of shortest paths to discover (default is 100).

    Returns:
    - numpy.ndarray: An array containing tuples representing discovered paths.
    """
```

## Parameters

- **graph (dict):** The input graph represented as a dictionary, where keys are nodes, and values are dictionaries of neighbors with associated weights.

- **source (hashable):** The starting node for the Dijkstra's algorithm.

- **n_neigh (int, optional):** The maximum number of shortest paths to discover (default is 100).

## Returns

The function returns a NumPy array containing tuples, where each tuple represents a discovered path. Each tuple consists of the following elements:

1. **Source Node:** The starting node of the path.
2. **Current Node:** The node reached in the discovered path.
3. **Distance:** The total distance of the discovered path from the source node.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Author

Chenwei Zhang [chwzhan@gmail.com](mailto:chwzhan@gmail.com)