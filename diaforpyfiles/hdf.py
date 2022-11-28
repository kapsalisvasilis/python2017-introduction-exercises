def union(lst):

    u = set()

    for s in lst:

        u = u | s

    return u


lst=[{1,2,3}, {3,4}, {4,5,6,7}, {6,7,8,9}]

print(union(lst))
