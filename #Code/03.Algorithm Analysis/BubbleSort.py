# filename: BubbleSort

from time import time

def BubbleSort(L):
    for i in range(0,len(L)-1):
        for j in range(i + 1,len(L)):
            if L[i] < L[j]:
                L[i],L[j] = L[j],L[i]
    return L

a = list(range(5000))
print("Length of list a is: ",len(a))
begin = time()
BubbleSort(a)
end = time()
print("Time: ",end - begin)