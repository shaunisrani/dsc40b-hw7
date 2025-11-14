from collections import deque
import dsc40graph

def biggest_descendent(graph, root, value):
    """
    Computes the biggest descendant value for every node in the tree.
    
    Parameters:
        graph (dsc40graph.DirectedGraph): The input graph representing a tree.
        root (int/str): The label of the root node.
        value (dict): A dictionary mapping node labels to their integer values.
        
    Returns:
        dict: A dictionary mapping each node label to its biggest descendant value.
    """
    
    # This dictionary will store the final answer for every node
    results = {}

    def dfs(u):
        # 1. Start with the value of the current node 'u'.
        # (The problem states 'u' is a scendant of itself)
        current_max = value[u]
        
        # 2. Explore all children (neighbors) of 'u'
        # We assume the dsc40graph object has a .neighbors() method
        for v in graph.neighbors(u):
            # Recursively find the max value in the child's subtree
            child_subtree_max = dfs(v)
            
            # 3. Update current_max if the child's subtree has a larger value
            if child_subtree_max > current_max:
                current_max = child_subtree_max
        
        # 4. Store the result for this node
        results[u] = current_max
        
        # 5. Return the max up the chain to the parent
        return current_max

    # Start the recursion from the root provided
    dfs(root)
    
    return results

if __name__ == "__main__":
    # Create the graph instance
    g = dsc40graph.DirectedGraph()

    # Define the edges from your screenshot example
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (4, 9), (3, 6), (3, 7)]

    # Add edges to the graph
    for edge in edges:
        g.add_edge(*edge)

    # Define the values from your screenshot example
    value = {
        1: 2, 
        2: 1, 
        3: 4, 
        4: 8, 
        5: 5, 
        6: 2, 
        7: 10, 
        8: 3, 
        9: 9
    }

    # Run the function
    result = biggest_descendent(g, 1, value)

    # Verify against the expected output
    expected = {1: 10, 2: 9, 3: 10, 4: 9, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}
    print("Result:", result)
    print("Matches Expected:", result == expected)