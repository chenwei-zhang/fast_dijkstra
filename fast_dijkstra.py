# fast_dijkstra/fast_dijkstra.py
__version__ = '0.1.0'

import heapq

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
    
    # Initialize data structures
    visited = set()
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    priority_queue = [(0, source)]
    paths = []

    # Main loop
    while priority_queue and len(paths) < n_neigh:
                
        _, current_node = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                tentative_distance = distances[current_node] + weight['weight']

                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heapq.heappush(priority_queue, (tentative_distance, neighbor))
                            
        paths.append((source, current_node, distances[current_node]))
        
    return paths