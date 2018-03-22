# 7.3.2 Implementing a Deque with a Double Linked List

class _DoubleLinkedBase:
    '''A base class providing a doubly linked list representation.'''
    
    class _Node:
        '''Lightweight, nonpublic class for storing a doubly linked node.'''
        __slots__ = '_element','_prev','_next'  # streamline memory
        
        def __init__(self,element,prev,next):   # initialize node's fields
            self._element = element             # user's element
            self._prev = prev                   # previous node reference
            self._next = next                   # next node reference

    def __init__(self):
        '''Create an empty list.'''
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer      # trailer is after header
        self._trailer._prev = self._header      # header is before trailer
        self._size = 0                          # number of element

    def __len__(self):
        '''Return the number of elements in the list.'''
        return self._size

    def is_empty(self):
        '''Return True if list is empty.'''
        return self._size == 0

    def _insert_between(self,e,predecessor,successor):
        '''Add element e between twm existing nodes and return new node.'''
        newest = self._Node(e,predecessor,successor)    # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self,node):
        '''Delete nonsentinel node from the list and return its element.'''
        predecessor = node._prev
        successor = node._next
        predessor._next = successor
        successor._prev = predessor
        self._size -= 1
        element = node._element                     # record delete element
        node._prev = node._next = node._element = None  # deprecate node
        return element                              # return deleted element

class LinkedDeque(_DoubleLinkedBase):
    '''Double-ended queue implementation based on a doubly linked list.'''
    
    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element      # real item just after header
    
    def last(self):
        '''Return (but do not remove) the element at the back of the deque.'''
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element     # real item just before trailer
    
    def insert_first(self,e):
        '''Add an elelment to the front of the deque.'''
        self._insert_between(e,self._header,self._header._next)     # after header
    
    def insert_last(self,e):
        '''Add an element to the back of the deque.'''
        self._insert_between(e,self._trailer._prev,self._trailer)   # before trailer
    
    def delete_first(self):
        '''Remove and return the element from the front of the deque.
        
        Raise Empty exception if the deque is empty.
        '''
        if self.is_empty():
            raise Empty("Deque is empty");
        return self._delete_node(self._header._next)    # use inherited method
    
    def delete_last(self):
        '''Remove and return the element from the back of the deque.
        
        Raise Empty exceptionif the deque is empty.
        '''
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)   # use inherited method