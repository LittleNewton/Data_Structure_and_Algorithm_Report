# 4.1.3 Binary Search

def binary_search(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid + 1, high)

#------------------------------ my main function ------------------------------
a = [1,2,3,5,8,15,45,666,3333,6222,9111]
print(binary_search(a,9111,0,11))