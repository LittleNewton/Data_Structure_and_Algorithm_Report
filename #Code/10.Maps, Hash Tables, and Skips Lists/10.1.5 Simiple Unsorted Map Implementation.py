# 10.1.5 Simiple Unsorted Map Implementation

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

class UnsortedTableMap(MapBase):
    """Map implementation usiong an unordered list."""
    
    def __init__(self,):
        """Create an empty map."""
        self._table = []
    
    def __getitem__(self,k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('key Error: ' + repr(k))
    
    def __setitem__(self,k,v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:        # Found a match
            if k == item._key:          # reassign a value
                item._value = value     # and quit
                return
        # did not find match for key
        self._table.append(self._Item(k,v))

    def __delitem__(self,k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:        # found a match
                self._table.pop(j)              # remove item
                return 
        raise KeyError('Key Error: ' + repr(k))
    
    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)
    
    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key                     # yield the KEY

#----------------------------- my main function -----------------------------
a = UnsortedTableMap()

a.__setitem__('LiuPeng','A')
a.__setitem__('LiYue','B')
a.__setitem__('God','C')

c = a.__iter__()
for k in c:
    print('(',k,',',a.__getitem__(k),')')
print(a.__len__())
a.__delitem__('LiYue')
c = a.__iter__()
for k in c:
    print('(',k,',',a.__getitem__(k),')')
print(a.__len__())