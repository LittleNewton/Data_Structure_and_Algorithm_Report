# 5.3.0 Dynamic Arrays and Amortization

import sys                      # provides getsizeof function
data = []
for k in range(20):             # NOTE: must fix choice of n
    a = len(data)               # number of elements
    b = sys.getsizeof(data)     # actual size in bytes
    print('Length:{0:3d}; Size in bytes:{1:4d}'.format(a,b))
    data.append(None)           # increase by one