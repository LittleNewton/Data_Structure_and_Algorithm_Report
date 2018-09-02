# 8.1.3 Computing Depth and Height

class Tree:
    """Abstract base class representing a tree structure."""

    #----------------------- nested Position class -----------------------
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

#----------------------------- my main function -----------------------------
