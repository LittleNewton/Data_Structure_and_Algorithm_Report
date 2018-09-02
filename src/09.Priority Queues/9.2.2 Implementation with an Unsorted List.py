# 9.2.2 Implementation with an Unsorted List

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

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):        # nonpublic utility
        """Return Position of item with minimun key."""
        if self.is_empty():         # is_empty inherited from base class
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of the items in the priority queue."""
        return len(self.data)

    def add(self,key,value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key,value))

    def min(self):
        """Return but do not remove(k,v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key,item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key,item._value)

#----------------------------- my main function -----------------------------