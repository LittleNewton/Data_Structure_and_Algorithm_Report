# 2.3.4 Iterators

class SequenceIterator:
    def __init__(self,sequence):
        self._seq = sequence
        self._k = -1
    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration('End')
    def __iter__(self):
        return self

#------------------------------ my main function ------------------------------
seq = [1,1,2,3,5,8]
print('0: ',seq)
s = SequenceIterator(seq)

print('1: ',end='')
for i in range(6):
    print(s.__next__(),' ',end='')
print('')

s._k = -1
for i in range(6):
    s._seq[i] += 2.718281828

print('2: ',seq)

print('3: ',end='')
s._k = -1
for i in range(6):
    print(s.__next__(),' ',end='')
