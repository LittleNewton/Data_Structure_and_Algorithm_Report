# 10.1.3 Python's MutableMapping Abstract Base Class

from collections import MutableMapping


def __contains__(self,k):
    try:
        self[k]     # access via __getitem__ (ignore result)
        return True
    except KeyError:
            return False    # attempt failed

def setdefault(self,k,d):
    try:
        return self[k]      # if __getitem__ succeeds, return values
    except KeyError:        # otherwise
        self[k] = decode    # set default value with __setitem__
        return decode       # and return that newly assigned value