# 10.5.2 Python's MutableSet Abstract Base Class

def __lt__(self,other): # subpports syntax S < T
    """Return true if this set is a proper subset of other."""
    if len(self) >= len(other):
        return False    # proper subset must have strictly
    for e in self:
        if e not in other:
            return False    # not a subset since element missing from other
    return True             # success; all conditions are met

def __or__(self,other):     # supports syntax  S | T
    """Return a new set that is the union of two existing sets."""
    result = type(self)()   # create new instance of concrete class
    for e in self:
        result.add(e)
    for e in other:
        result.add(e)
    return result

def __ior__(self,other):    # supports syntax S |= T
    """Modify this set to be the union of itself an another set."""
    for e in other:
        self.add(e)
    return self             # technical requirement of in-place operator