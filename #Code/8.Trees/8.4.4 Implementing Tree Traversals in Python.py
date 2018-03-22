# 8.4.4 Implementing Tree Traversals in Python

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""
    
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element','_next'          # streamline memory usage
        
        def __init__(self,element,next):        # initialize node's field
            self._element = element             # reference to user's element
            self._next = next                   # reference to next node

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0                          # number of queue elements

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
        return self._head._element              # front aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                     # special case as queue is empty
            self._tail = None                   # removed head had been the tail
        return answer

    def enqueue(self,e):
        """Add an element to the back of queue."""
        newest = self._Node(e,None)             # node will be new tail node
        if self.is_empty():
            self._head = newest                 # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                     # update reference to tail node
        self._size += 1

class Tree:
    """Abstract base class representing a tree structure."""

    #------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self,other):
            """Return True if other Positon represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self,other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    #---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self,p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self,p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self,p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    #---------- concrete methods implemented in this class ----------
    def is_root(self,p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self,p):
        """Return True if Positoin p does not have any children."""
        return self.num_children == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    #---------- new methods in this section ----------
    def depth(self,p):
        """Return the number of levels separating Positon p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):             # works, but O(n^2) worst-case time
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self,p):
        """Ruturn the height of the subtree rooted at Postion p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self,p=None):
        """Return the height of the subtree rooted ar Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)             # start _height2 recursion
    
    #---------- new method in this section ----------
    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.position():       # use same order as position()
            yield p.element()           # but yield each element

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):   # start recursion
                yield p

    def _subtree_preorder(self,p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p                                             # visit p before its subtrees
        for c in self.children(p):                          # # for each child c
            for other in self._subtree_preorder(c):         # do preorder of c's subtree
                yield other                                 # yielding each to our caller

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()                              # return entire preorder iteration

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):   # start recursion
                yield p

    def _subtree_postorder():
        """Generate a postorder iteration of postions in subtree rooted at p."""
        for c in self.children(p):                          # for each child c
            for other in self._subtree_postorder(c):        # do postorder of c's subtree
                yield other                                 # yielding each to our caller
        yield p                                             # visit p after its subtrees
    
    def breathfirst(self):
        """Generate a breath-first iteration of the positions of the tree."""
        if not self.is_empty():
            finge = LinkedQueue()                           # known positions not yet yielded
            fringe.enqueue(self.root)                       # starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue()                        # renove from front of the queue
                yield p                                     # report this position
                for c in self.children(p):
                    fringe.enqueue(c)                       # add children to back of queue

class BinaryTree(Tree):
    """Abstract base class representint a bianry tree structure."""

    #--------------------- additional abstract methods ---------------------
    def left(self,p):
        """Return a Position representing p's left child.

        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self,p):
        """Return a Position representing p's right child.

        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclass')

    #---------- concrete methods implemented in this class ----------
    def sibling(self,p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                      # p must be the root
            return None                         # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)       # possibly None
            else:
                return self.left(parent)        # possibly None

    def children(self,p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self,p):
        """Generate an inorder iteration of positinos in subtree rooted at p."""
        if self.left(p) is not None:            # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield p
        yield p                                 # visit p between its subtrees
        if self.right(p) is not None:           # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other
    
    # override inherited version to make inorder the default
    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()                   # make inorder the default