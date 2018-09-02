# 7.5.0 Sorting a Positional List

def insertion_sort(L):
    """Sort PositionalList o comparablde elements into nondecreasing order."""
    if len(L) > 1:                      # otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)     # next item to place
            value = pivot.element()
            if value > marker.element():# pivot is already sorted
                marker = pivot          # pivot becomes new marker
            else:                       # must relocate pivot
                walk = marker           # find leftmost item greater than value
                while walker != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk,value)# reinsert value before walk

#----------------------------- my main function -----------------------------