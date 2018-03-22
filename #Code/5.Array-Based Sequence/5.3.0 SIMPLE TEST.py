# 5.3.0 Dynamic Arrays and Amortization

import sys
data = []
for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length:{0:3d}; Size in bytes:{1:4d}'.format(a,b))
    data.append(None)