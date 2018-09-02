# Quick Sort for a list

from time import time
import sys   
sys.setrecursionlimit(1000000)

def QuickSort(L):
    L_Left = []
    L_Right = []
    L_Middle = []
    if len(L) <= 1:
        return L
    else:
        for i in L:
            pivot = (L[0] + L[-1] + L[len(L)//2])/3
            if i > pivot:
                L_Left.append(i)
            elif i < pivot:
                L_Right.append(i)
            else:
                L_Middle.append(i)
    L_Left = QuickSort(L_Left)
    L_Right = QuickSort(L_Right)
    return L_Left + L_Middle + L_Right

A = list(range(3500))
print(A)
print("Length of list a is: ",len(A))
begin = time()
A = QuickSort(A)
end = time()
print("Time: ",end - begin)
print(A)