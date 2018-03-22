# 14.2.5 Python Implementation

class Graph:
    """Representation of a simple graph using an adjacency map."""

    #------------------------- nested Vertex class -------------------------
    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'

        def __init__(self,x):
            """Do not call constructor directly.
            Use Graph's insert_vertex(x).
            """
            self._element = x

        def element(self):
            """Return element associated with this vertex."""
            return self._element

        def __hash__(self):         #  will allow vertex to be a map/set key
            return hash(id(self))

    #------------------------- nested Edge class -------------------------
    class Edge:
        """Lightweight edge structure for a graph."""
        __slot__ = '_origin','_destination','_element'

        def __init__(self,u,v,x):
            """Do not call constructor directly.
            Use Graph's insert_edge(u,v,x).
            """
            self._origin = u
            self._destination = v
            self._element = x
            
        def endpoints(self):
            """Return (u,v) tuple for vertices u and v."""
            return (self._origin,self._destination)

        def opposite(self,v):
            """Return the vertex that is opposite v on this edge."""
            return self._destination

        def element(self):
            """Return element associated with this edge."""
            return self._element

        def __hash__(self):         # will allow edge to be a map/set key
            return hash((self._origin,self._destination))

    #------------------------- Graph class -------------------------
    def __init__(self,directed=False):
        """Create an empty graph (undirected, by default).

        Graph is directed if optional parameter is set to True.
        """
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """Return True if this is a directed graph; False if undirected.

        Property is based on the original declaration of the graph, not its 
        contents.
        """
        return self._incoming is not self._outgoing
        """ directed if maps are distinct"""

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return a set of all edges of the graph."""
        result = set()      # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())   # add edges to resulting set
        return result

    def get_edge(self,u,v):
        """Return the edge from u to v, or None if not adjacent."""
        return self._outgoing[u].get(v)
    
    def degree(self,v,outgoing=True):
        """Return number of (outgoing) edges incident to vertex v in the graph.

        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self,v,outgoing=True):
        """Return all (outgoing) edges incedent to vertex v in the graph.

        If graph is directed, optional parameter used to request incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[j].values():
            yield edge

    def insert_vertex(self,x=None):
        """Insert and return a new Vertex with element x."""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}      # need distinct map for incoming edges
        return v

    def insert_edge(self):
        """Insert and return a new Edge from u to v with auxiliary element x."""
        e = self.Edge(u,v,x)
        self._outgoing[u][v] = e
        self._incoming[u][v] = e

#------------------------------ my main function ------------------------------
