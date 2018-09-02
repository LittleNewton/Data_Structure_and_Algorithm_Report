# 12.2.5 Alternative Implementation of Merge_Sort

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element','_next'      # streamline memory usage

        def __init__(self,element,next):    # initialize node's field
            self._element = element         # reference to user's element
            self._next = next               # reference to next node

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0                      # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element          # front aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                 # special case as queue is empty
            self._tail = None               # removed head had been the tail
        return answer

    def enqueue(self,e):
        """Add an element to the back of queue."""
        newest = self._Node(e,None)         # node will be new tail node
        if self.is_empty():
            self._head = newest             # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                 # update reference to tail node
        self._size += 1

def merge(S1,S2,S):
    """Merge two sorted queue instances S1 and S2 into empty queue S."""
    while not S1.is_empty() and not S2.is_empty():
        if  S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():        # move remaining elements of S1 to S
        S.enqueue(S1.dequeue())
    while not S2.is_empty():
        S.enqueue(S2.dequeue())

def merge_sort(S):
    """Sort the elements of queue S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return                      # list is already sorted
    # divide
    S1 = LinkedQueue()              # or any other queue implementation
    S2 = LinkedQueue()
    while len(S1) < n //2:          # move the first n //2 elements to S1
        S1.enqueue(S.dequeue())
    while not S.is_empty():         # move the rest to S2
        S2.enqueue(S.dequeue())
    # conquer (with recursion)
    merge_sort(S1)      # sort first half
    merge_sort(S2)      # sort second half
    # merge results
    merge(S1,S2,S)      # merge sorted halves back into S