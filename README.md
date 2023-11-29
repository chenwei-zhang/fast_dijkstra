# Fast-Dijkstra: Dijkstra's N-Shortest Paths Finder

[![](https://img.shields.io/badge/fast__dijkstra-0.1.0-gold)](https://anaconda.org/ChenweiZhang/fast_dijkstra)
![](https://anaconda.org/chenweizhang/fast_dijkstra/badges/latest_release_date.svg)
![](https://anaconda.org/chenweizhang/fast_dijkstra/badges/platforms.svg)
![](https://anaconda.org/chenweizhang/fast_dijkstra/badges/license.svg)
![](https://anaconda.org/chenweizhang/fast_dijkstra/badges/downloads.svg)

## Overview

The `fast_dijkstra` package is a Python implementation of Dijkstra's algorithm to find a specified number of shortest paths (top K) in a weighted graph. \
The script defines a function dijkstra_n_shortest_paths that efficiently computes a specified number of shortest paths in a weighted graph using Dijkstra's algorithm, returning the paths as an array of tuples.

## Quick installation
```bash
conda install -c chenweizhang fast_dijkstra
```

## Local GitHub installation

```bash
# clone project   
git clone https://github.com/chenwei-zhang/fast_dijkstra

# install vida (recommond install in a virtual environment) 
conda activate <myenv>
cd fast_dijkstra
conda update pip -y
pip install -e .   
```

## Usage

```python
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
    - List: A list containing tuples representing discovered paths.
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
