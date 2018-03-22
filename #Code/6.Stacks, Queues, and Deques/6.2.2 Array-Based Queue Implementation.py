# 6.2.2 Array-Based Queue Implementation

class ArrayQueue:
    """FIFO queue implementation using a  Python list as underlying storage."""
    DEFAULT_CAPACITY = 10               # moderate capacity for all new queues
    
    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of element in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue if empty."""
        return self._size == 0

    def first(self):
        """Return  (but do not remove) the element at the front of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is emppty')
        return self._data[self._front]
    
    def dequence(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None                      # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enquence(self,e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))               # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self,cap):                                  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data                                    # keep track of existing list
        self._data = [None] * cap                           # allocate list with new capacity
        walk = self.front
        for k in range(self._size):                         # only consider existing elements
            self._data[k] = old[walk]                       # intentionally shift indices
            walk = (1 + walk) % len(old)                    # use old size as modules
        self._front = 0                                     # front has been realigned

#------------------------------ my main function ------------------------------
a = ArrayQueue()
print('1: ',a.__len__(),',front is',a._front)
a.enquence('LiuPeng')
print('2: ',a._data,', front is',a._front)
for i in range(9):
    a.enquence(i)
print('3: ',a._data,',front is',a._front)
a.dequence()
print('4: ',a._data,', front is',a._front)
a.dequence()
print('5: ',a._data,', front is',a._front)