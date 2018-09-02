# 5.3.3 Python's List Class

from time import time       # import time function from time module
def compute_average(n):
    """Perform n appends to an empty list and return average time elapsed."""
    data = []
    start = time()          # record the start time (in seconds)
    for k in range(n):
        data.append(None)
    end = time()            # record the end time (in seconds)
    return (end - start)/n  # compute average per operation

#----------------------------- my main function -----------------------------

a = []
n = 10000
while n <= 100000000:
    print(format(compute_average(n),'1.25f'))
    n *= 10