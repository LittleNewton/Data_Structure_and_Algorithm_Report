# 8.4.5 Applications of Tree Traversals

# This is an collection of several functions related to
# Tree Traversal. Maybe they are very useful

#---------- Application 1 ----------
# Table of contects

def preorder_indent(T,p,d):
    """Print preorder representation of subtree of T rooted at p at deepth d."""
    print(2 * d * ' ' + str(p.element()))       # use depth for indentation
    for c in T.children(p):
        preorder_indent(T,p,d+1)                # child depth is d+1

def preorder_label(T,p,d,path):
    """Print labeled representation of subtree of T rooted at p at depth d."""
    label = '.'.join(str(j+1) for j in path)    # displayed labels are one-indexed
    print(2 * d * ' ' + label,p.element())
    path.append(0)                              # path entries are zero-indexed
    for c in T.children(p):
        preorder_label(T,c,d+1,path)            # child depth is d+1
        path[-1] +=1
    path.pop()

#---------- Application 2 ----------
# Parenthetic Representations of a Tree
def parenthesize(T,p):
    """Print parenthesized representation of subtree of T rooted at p."""
    print(p.element,end='')                     # use of end avoids trailing newline
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = '£¨' if first_time else '£¬'        # determine proper separator
            print(sep,end='')
            first_time = False                          # any future passes will not be the first
            parenthesize(R,c)                           # recur on child
        print('£©',end='')                               # include closing parenthesis

#---------- Application 3 ----------
# Computing Disk Space
def disk_space(T,p):
    """Return total disk space for subtree of T rooted at p."""
    subtotal = p.element().space()              # space used at position p
    for c in T.children(p):
        subtotal += disk_space(T,c)             # add child's space to subtotal
    return subtotal