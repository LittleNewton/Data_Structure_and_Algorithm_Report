# 2.3.5 Example: Range Class

class Range:
    def __init__(self,start,stop=None,step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start,stop = 0,start
        self._length = max(0,(stop - start + step - 1)//step)
        self._start = start
        self._step = step
    def __len__(self):
        return self._length
    def __getitem__(self,k):
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        return self._start + k * self._step

#------------------------------ my main function ------------------------------
print(range(2,5))
dd = Range(2,5,1)
for i in Range(0,3):
    print(dd[i])
print('----------------------')
print(dd.__getitem__(2))
