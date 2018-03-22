# 14.7.1 Prim-Jarnik Algorithm

def MST_PrimJarnik(g):
    """Compute a minimum spanning tree of weighted graph g.
    
    Return a list of edges that comprise the MST (in arbitrary order).
    """
    d = {}      # d[v] is bound on distance to tree
    tree = []   # list of edges in spanning tree
    pq = AdaptableHeapPriorityQueue()   # d[v] maps to value (v,e = (u,v))
    pqlocator = {}  # map from vertex to its pq locator
    
    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if len(d) == 0:         # this is the first node
            d[v] = 0            # make it the root
        else:
            d[v] = float('inf') # positive infinity
        pqlocator[v] = pq.add(d[v],(v,None))
    
    while not pa.is_empty():
        key,value = pq.remove_min()
        u,edge = value  # unpack tuple from pq
        del pqlocator[u]    # u is no longer in pq
        if edge is not None:
            tree.append(edge)   # add edge to tree
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator:  # thus v not yet in tree
                # see if edge (u,v) better connects v to the growing tree
                wgt = link.element()
                if wgt < d[v]:      # better edge to v?
                    d[v] = wgt      # update the distance
                    pq.update(pqlocator[v],d[v],(v,link))   # update the pq entry
    return tree