# Quick Sort for a list

def QuickSort(L):
    L_Left = []
    L_Right = []
    L_Middle = []
    if len(L) <= 1:
        return L
    else:
        for i in L:
            if i < L[0]:
                L_Left.append(i)
            elif i > L[0]:
                L_Right.append(i)
            else:
                L_Middle.append(i)
    L_Left = QuickSort(L_Left)
    L_Right = QuickSort(L_Right)
    return L_Left + L_Middle + L_Right

a = [1,96,88,75,42,16,59,888,999,100]
print(QuickSort(a))