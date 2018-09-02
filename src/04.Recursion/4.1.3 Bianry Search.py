# 4.1.3 Binary Search

def binary_search(data,target,low,high):
    """Return True if target is found in indicated portion of a Python list.

    The search only considers the protion from data[low] to data[high] inclusive
    """
    if low > high:                      # interval is empty; no match
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:         # found a match
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data,target,low,mid-1)
        else:
            # recur on the portion right of the middle
            return binary_search(data,target,mid + 1, high)

#----------------------------- my main function -----------------------------
a = [1,2,3,5,8,15,45,666,3333,6222,9111]
print(binary_search(a,9111,0,11))