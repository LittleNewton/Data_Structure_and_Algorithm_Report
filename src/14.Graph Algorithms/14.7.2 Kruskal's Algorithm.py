# 14.7.2 Kruskal's Algorithm

class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key','_value'

        def __init__(self,k,v):
            self._key = k
            self._value = v

        def __It__(self,other):
            return self._key < other._key   # compare items vased on their keys

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self) == 0

class HeapPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with a bianry heap."""
    #--------------- nonpublic behaviors ---------------
    def _parent(self,j):
        return (j-1)//2

    def _left(self,j):
        return 1 * j + 1

    def _right(self,j):
        return 2 * j +2

    def _has_left(self,j):
        return self._left(j) < len(self._data)  # index beyond end of list?

    def _has_right(self,j):
        return self._right(j) < len(self._data) # index beyond end of list?

    def _swap(self,i,j):
        """Swap the elements at indices i and j of array."""
        self._data[i],self._data[j] = self._data[j],self._data[i]

    def _upheap(self,j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j,parent)
            self._upheap(parent)    # recur at position of parent

    def _downheap(self,j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left      # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j,small_child)
                self._downheap(small_child) #recur at position of small child

    #--------------- public behaviors ---------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self,key,value):
        """Add a key-value pair to the priority queue."""
        self._dat.append(self._Item(key,value))
        self._upheap(len(self._data) - 1)   # upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key,item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
        
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0,len(self._data) - 1)   # put minimum item at the end
        item = self._data.pop()             # and remove it from the list;
        self._downheap(0)                   # then fix new root
        return (item._key,item._value)

def MST_Kruskal(g):
    """Compute a minimun spanning tree of a graph using Kruskal's algorithm.
    
    Return a list of edges that comprise the MST.
    
    The elements of the graph's edges are assumed to be weights.
    """
    tree = []       # list of edges in spanning tree
    pa = HeapPriorityQueue()    # entries are edges in G, with weights as key
    forest = Partition()        # keeps track of forest clusters
    position = {}               # map each node to its Partition entry
    
    for v in g.edges():
        position[v] = forest.make_group(v)
    
    for e in g.edges():
        pq.add(e,element(),e)   # edge's element is assumed to be its weight
    
    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():
        # tree not spanning and unprocessed edges remain
        weight,edge = pq.remove_min()
        u,v = edge.endpoints()
        a = forest .find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a,b)
    
    return tree