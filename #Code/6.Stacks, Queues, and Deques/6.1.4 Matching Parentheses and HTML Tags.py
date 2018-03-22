# 6.1.4 Matching Parentheses and HTML Tags

    # 6.1.4.1 An Algorithm for Matching delimiters
    # 6.1.4.2 Matching Tags in a Markup Language

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

def is_amtched_html(raw):
    """Return True if all HTML tags are preperly match; False otherwise."""
    S = ArrayStack()
    j = raw.find('<>')              # find first '<' character (if any)
    while j != -1:
        k = raw.find('>',j+1)       # find next '>' character
        if k ==1:
            return False            # invalid tag
        tag = raw[j+1:k]            # strip away < >
        if not tag.startswith('/'): # this is opening tag
            S.push(tag)
        else:                       # this is closing tag
            if S.is_empty():
                return False        # nothing to match with
            if tag[1:] != S.pop():
                return False        # mismatched delimiter
        j = raw.find('<',k+1)       # find next '<' character (if any)
    return S.is_empty               # were all opening tags matched?

def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['                   # opening delimiters
    righty = ')}]'                  # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)               # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False        # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False        # mismatched
    return S.is_empty()             # were all symbols matched

#------------------------------ my main function ------------------------------
test = '{[(1 + x) * c - (d - e)] / m} + q'
print(is_matched(test))

