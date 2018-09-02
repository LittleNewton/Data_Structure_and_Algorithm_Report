# 12.2.5 Alternative Implementation of Merge-Sort

"""A Bottom-Up(Nonrecursive) Merge-Sort"""

def merge(src,result,start,inc):
    """Merge src[start:start+inc] and src[start+inc:start+2*inc] into result.""" 
    end1 = start + inc                  # boundary for run 1
    end2 = min(start+2*inc,len(src))    # boundary for run 2
    x,y,z = start,start + inc,start     # index into run 1 and run 2, result