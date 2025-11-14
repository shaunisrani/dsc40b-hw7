import collections

class DirectedGraph:
    """
    A simple implementation of a directed graph using an adjacency list.
    """
    def __init__(self):
        self.adj = collections.defaultdict(list)
        self._nodes = set()

    def add_edge(self, u, v):
        """Adds a directed edge from node u to node v."""
        self.adj[u].append(v)
        self._nodes.add(u)
        self._nodes.add(v)

    def neighbors(self, u):
        """Returns the neighbors of node u in ascending order."""
        # The homework specifies neighbors should be produced in ascending order
        return sorted(self.adj[u])

    @property
    def nodes(self):
        """Returns a set of all nodes in the graph."""
        return self._nodes

class UndirectedGraph:
    """
    A simple implementation of an undirected graph.
    (You will need this for Problem 2: Clustering)
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

    def neighbors(self, u):
        """Returns the neighbors of node u in ascending order."""
        return sorted(self.adj[u])

    @property
    def nodes(self):
        """Returns a set of all nodes in the graph."""
        return self._nodes