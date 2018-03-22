# 2.3.4 Iterators

class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self,sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence    # keep a reference to the underlying data
        self._k = -1            # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1                    # advance to next index
        if self._k < len(self._seq):
            return(self._seq[self._k])  # return the data element
        else:
            raise StopIteration('End')  # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

#----------------------------- my main function -----------------------------
seq = [1,1,2,3,5,8]             # seq is iterable object instance
seq_buildIn = [1,1,2,3,5,8]     # seq_buildIn is the same with seq
print('0: ',seq)    
s = SequenceIterator(seq)
s_buildIn = seq_buildIn.__iter__()

print('1: ',end='')
for i in range(6):
    print(s.__next__(),' ',end='')
print('')

print('2: ',end='')
for i in range(6):
    print(s_buildIn.__next__(),' ',end='')
print('')

s._k = -1
for i in range(6):
    s._seq[i] += 2.718

print('3: ',seq)

print('4: ',end='')
s._k = -1
for i in range(6):
    print(s.__next__(),' ',end='')