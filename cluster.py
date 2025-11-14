from collections import deque
import dsc40graph

def cluster(graph, weights, level):
    """
    Computes the clusters of a weighted, undirected graph based on a 
    similarity level.
    
    A cluster is a connected component where all edges in the connecting 
    paths have a weight >= level.
    
    Parameters:
        graph (dsc40graph.UndirectedGraph): The input graph.
        weights (function): A function weights(u, v) that returns the 
                            weight of the edge (u, v).
        level (float or int): The minimum similarity level to consider 
                              an edge as part of a cluster.
                              
    Returns:
        frozenset: A frozenset containing frozensets. Each inner 
                   frozenset represents a single cluster of nodes.
    """
    
    # A set to store all nodes that we have already visited
    visited = set()
    
    # A set to store the final clusters (as frozensets)
    all_clusters = set()
    
    # We must check every node in the graph
    for node in graph.nodes:
        
        # If we have already visited this node, it's part of a
        # cluster we've already found. We can skip it.
        if node in visited:
            continue
            
        # If the node is unvisited, it's the start of a new cluster.
        # We will use BFS (Breadth-First Search) to find all nodes
        # connected to it *above the given level*.
        
        current_cluster = set()
        q = deque([node])
        visited.add(node)
        
        while q:
            current_node = q.popleft()
            current_cluster.add(current_node)
            
            # Check all neighbors of the current node
            for neighbor in graph.neighbors(current_node):
                
                # THIS IS THE KEY: Only "cross" the edge if its
                # weight is >= level
                if weights(current_node, neighbor) >= level:
                    
                    # If the neighbor is valid (above level) and
                    # we haven't seen it yet, add it to our search.
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                        
        # The queue is empty, so we've found every node in this
        # component. Add the completed cluster to our set of clusters.
        all_clusters.add(frozenset(current_cluster))
        
    # After iterating through all nodes, return the final result.
    return frozenset(all_clusters)

if __name__ == "__main__":
    
    # 1. Create the graph
    g = dsc40graph.UndirectedGraph()
    edges = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd')]
    for u, v in edges:
        g.add_edge(u, v)

    # 2. Define the weights function (as specified in the prompt)
    def weights(x, y):
        x, y = (x, y) if x < y else (y, x)
        weight_map = {
            ("a", "b"): 1, 
            ("b", "c"): 0.3, 
            ("c", "d"): 0.9, 
            ("a", "d"): 0.2
        }
        return weight_map[(x, y)]

    # 3. Run the cluster function with level = 0.4
    level = 0.4
    result = cluster(g, weights, level)
    
    print(f"Graph nodes: {g.nodes}")
    print(f"Level: {level}\n")
    print("Result:")
    print(result)

    # 4. Verify the output
    expected = frozenset([frozenset(['a', 'b']), frozenset(['c', 'd'])])
    print("\nMatches Expected:", result == expected)

    # --- Another Test Case ---
    level_low = 0.1
    result_low = cluster(g, weights, level_low)
    print(f"\nTest with level = {level_low}:")
    print(result_low)
    expected_low = frozenset([frozenset(['a', 'b', 'c', 'd'])])
    print("Matches Expected:", result_low == expected_low)