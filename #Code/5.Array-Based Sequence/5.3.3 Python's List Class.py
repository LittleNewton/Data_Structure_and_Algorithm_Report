# 5.3.3 Python's List Class

from time import time

def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start)/n

print(compute_average(10000))