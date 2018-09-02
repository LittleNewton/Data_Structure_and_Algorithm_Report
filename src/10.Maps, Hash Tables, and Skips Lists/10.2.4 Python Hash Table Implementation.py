# 10.2.4 Python Hash Table Implementation

from collections import MutableMapping

class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class."""

    #----------------------- nested _Item class -----------------------
    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = '_key','_value'

        def __init__(self,k,v):
            self._key = k
            self._value = v

        def __eq__(self,other):
            return self._key == other._key  # compare items vased on their keys

        def __ne__(self,other):
                return not (self == other)      # opposite of __eq__

        def __It__(self,other):
            return self._key < other._key# compare items based on their keys

class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""
    
    def __init__(self,cap=11,p=109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0                         # number of entries in the map
        self._prime = p                     # prime for MAD compression
        self._scale = 1 + randrange(p-1)    # scale from 1 to p-1 for MAD
        self._shift = randrange(p)          # shift from 0 to p-1 for MAD
    
    def _hash_function(self,k):
        return (hash(k) * self._scale + self._shift) %\
        self._prime % len(self._table)
    
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        j = self._hash_function(k)
        return self._bucket_setitem(j,k)    # may raise KeyError
    
    def __setitem__(self,k,v):
        j = self._hash_function(l)
        self._bucket_setitem(j,k,v)         # subroutine maintains self._n
        if self._n > len(self._table) // 2: # keep load factor <= o.5
            self._resize(2 * len(self._table) - 1)
            # number 2^x - 1 if often prime
    
    def __delitem__(self,k):
        j = self._hash_function(k)
        self._bucket_delitem(j,k)           # may raise KeyError
        self._n -= 1
    
    def _resize(self,c):                    # resize bucket array to capacity c
        old = list(self.items())        # use iteration to record existing items
        self._table = c * [None]        # then reset table to desired capacity
        self._n = 0                     # n recomputed during subsequent adds
        for (k,v) in old:
            self[k] = v                     # reinsert old key-value pair

class ChainHashMap(HashMapBase):
    """Hash map implemented with  separate chaining for collision resolution."""
    
    def _bucket_getitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))  # no match found
        return bucket[k]            # may raise KeyError
    
    def _bucket_setitem(self,j,k,v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap() # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:       # key was new to the table
            self._n += 1                        # increase overall map size
    
    def _bucket_delitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k)) # no match found
        del bucket[k]               # may raise KeyError
    
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:              # a nonempty slot
                for key in bucket:
                    yield key

class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    _AVAIL = object()      # sentinal marks location of previous deletions
    
    def _is_available(self,j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    
    def _find_slot(self,j,k):
        """Search for key k in bucket at index j.
        
        Return (succes, index) tuple, described as follows:
        If match was found, success if True and index denotes its location.
        If no match found, success is False and index denotes first
        available slot.
        """
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j          # mark this as first avail
                if self._table[j] is None:
                    return (False,firstAvail)   # search has failed
            elif k == self._table[j]._key:
                return (True,j)             # found a match
            j = (j + 1) % len(self._table)
    
    def _bucket_getitem(self,j,k):
        found,s = self._find_slot(j,k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no match found
        return self._table[s]._value
    
    def _bucket_setitem(self,j,k,v):
        found,s = self._find_slot(j,k)
        if not found:
            self._table[s] = self._Item(k,v)        # insert new item
            self._n += 1                            # size has increased
        else:
            self._table[s]._value = v               # overwrite existing
    
    def _bucket_delitem(self,j,k):
        found,s = self._find_slot(j,k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no match found
        self._table[s] = ProbeHashMap._AVAIL        # mark as vacated
    
    def __iter__(self):
        for j in range(len(self._table)):           # scan entire table
            if not self._is_available(j):
                yield self._table[j]._key