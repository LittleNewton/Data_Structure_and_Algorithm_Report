# 5.4.1 Efficency of Python's List and Tuple Classes

def insert(self,k,value):
    if self._n == self._capacity:
        self._resize(2 * self._capacity)
    for j in range(self._n,k,-1):
        self._A[j] = self._A[j-1]
    self._A[k] = value
    self._n += 1

def remove(self,value):
    for k in range(k,self._n):
        if self._A[k] == value:
            for j in range(k,self._n - 1):
                self._A[j] = self._A[j+1]
            self._A[self._n - 1] = None
            self._n -= 1
            return
    raise ValueError('value not found')