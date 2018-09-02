# 5.5.2 Sorting a sequence

def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1,len(A)):           # from 1 to n-1
        cur = A[k]                      # current element to be inserted
        j = k                           # find correct index j for current
        while j > 0 and A[j-1] > cur:   # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur                      # cur is now in the right place

#----------------------------- my main function -----------------------------

import random
a = [random.randint(0,100) for i in range(10)]
print('1:',a)
insertion_sort(a)
print('2:',a)