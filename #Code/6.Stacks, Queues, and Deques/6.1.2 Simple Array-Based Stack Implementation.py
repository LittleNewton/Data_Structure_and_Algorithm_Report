# 6.1.2 Simple Array-Based Stack Implementation

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []                         # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self,e):
        """Add element e to the top of the stack."""
        self._data.append(e)                    # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                   # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()                 # remove last item from list

#------------------------------ my main function ------------------------------
a = ArrayStack()
print('1: ',a.__len__())
a.push(8)
print('2: ',a._data)
a.push('LiuPeng')
print('3: ',a._data)
a.push('1 + 2 + 3')
print('4: ',a._data)
print('5: ',a.pop())