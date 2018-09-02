# 12.2.2 Array-Based Implementation of Merge-Sort

def merge_sort(S):
    """Sort the element of Python list S using the merge-sort algorithm."""
    m = len(S)
    if n < 2:
        return          # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]       # copy of first half
    S2 = S[mid:n]       # copy of second half
    # conquer (with recursion)
    merge_sort(S1)      # sort copy of first half
    merge_sort(S2)      # sort copy of second half
    # merge results
    merge(S1,S2,S)      # merge sorted halves back into S