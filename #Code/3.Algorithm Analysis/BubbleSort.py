# filename: BubbleSort

def BubbleSort(L):
    for i in range(0,len(L)-1):
        for j in range(i + 1,len(L)):
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]
    return L

a = [1,96,88,75,42,16,59]
print(BubbleSort(a))