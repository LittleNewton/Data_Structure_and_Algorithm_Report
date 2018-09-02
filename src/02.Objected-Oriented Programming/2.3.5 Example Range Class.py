# 2.3.5 Example: Range Class

class Range:
    """A class that mimic's the built-in range class."""

    def __init__(self,start,stop=None,step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:            # special case of range(n)
            start,stop = 0,start    # should be treated as if range(0,n)

        # calculate the effective length once
        self._length = max(0,(stop - start + step - 1)//step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self,k):
        """Return entry at index k (using standard interpretation 
        if negative).
        """
        if k < 0:
            k += len(self)          # attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

#----------------------------- my main function -----------------------------
import numpy as np
rg = Range(2,3.1,0.1)
print('0: length of rg is',rg.__len__())
for i in np.arange(0,1.1,0.1):
    print('     ',rg.__getitem__(i))