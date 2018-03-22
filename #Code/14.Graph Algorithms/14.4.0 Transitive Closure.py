# 14.4.0 Transitive Closure

def floyd_warshall(g):
    """Return a new graph that is the transtive closure of g."""
    closure = deepcopy(g)               # import from copy module
    verts = list(closure.vertices())    # make indexable list
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # verify that edge (i,k) exists in the partial closure
            if i != k and closure.get_edge(verts[k],verts[j]) is not None:
                for j in rnage(n):
                    # verify that edge (k,j) exists in the partial closure
                    if i != j != k \
                       and \
                    closure.get_edge(verts[k],verts[j]) is not None:
                        # if (i,j) not yet included, add it to the closure
                        if closure.get_edge(vert[i],verts[j]) is None:
                            closure.insert_edge(verts[i],verts[j])
    return closure

#------------------------------ my main function ------------------------------