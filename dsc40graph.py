import collections

class DirectedGraph:
    """
    A simple implementation of a directed graph.
    """
    def __init__(self):
        # Stores {node: [neighbor1, neighbor2]}
        self.adj = collections.defaultdict(list)
        # Stores all nodes, including those with no edges
        self._nodes = set()

    def add_edge(self, u, v):
        """Adds a directed edge from node u to node v."""
        self.adj[u].append(v)
        self._nodes.add(u)
        self._nodes.add(v)
    
    def add_node(self, u):
        """Adds a node to the graph."""
        if u not in self._nodes:
            self._nodes.add(u)
            # Ensures the node exists in the adjacency dict
            _ = self.adj[u]

    def neighbors(self, u):
        """Returns the neighbors of node u in ascending order."""
        # Use .get() for safety in case a node exists but has no outgoing edges
        return sorted(self.adj.get(u, []))

    @property
    def nodes(self):
        """Returns a set of all nodes in the graph."""
        return self._nodes

class UndirectedGraph:
    """
    A simple implementation of an undirected graph.
    (Needed for Programming Problem 2: Clustering)
    """
    def __init__(self):
        self.adj = collections.defaultdict(list)
        self._nodes = set()

    def add_edge(self, u, v):
        """Adds an undirected edge between u and v."""
        self.adj[u].append(v)
        self.adj[v].append(u)
        self._nodes.add(u)
        self._nodes.add(v)

    def add_node(self, u):
        """Adds a node to the graph."""
        if u not in self._nodes:
            self._nodes.add(u)
            # Ensures the node exists in the adjacency dict
            _ = self.adj[u]

    def neighbors(self, u):
        """Returns the neighbors of node u in ascending order."""
        return sorted(self.adj.get(u, []))

    @property
    def nodes(self):
        """Returns a set of all nodes in the graph."""
        return self._nodes