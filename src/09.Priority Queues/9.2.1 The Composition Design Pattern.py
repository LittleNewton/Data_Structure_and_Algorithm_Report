# 9.2.1 The Composition Design Pattern

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

#----------------------------- my main function -----------------------------