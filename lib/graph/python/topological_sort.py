def topological_sort(g: list[list[int]]):
    n = len(g)
    in_deg = [0]*n
    for v in range(n):
        for u in g[v]:
            in_deg[u] += 1
    
    stack = [v for v in range(n) if in_deg[v] == 0]
    order = []
    while stack:
        v = stack.pop()
        order.append(v)
        for u in g[v]:
            in_deg[u] -= 1
            if in_deg[u] == 0:
                stack.append(u)

    for v in range(n):
        if in_deg[v] != 0:
            return False

    return order


from sys import setrecursionlimit
setrecursionlimit(2**30)

def topological_sort(g: list[list[int]]):
    n = len(g)
    # identify roots
    roots = set(range(n))
    for i in range(n):
        for j in g[i]:
            roots.discard(j)
    
    if not roots:
        return False # not a dag

    topo_order = []
    visited = [False]*n
    rec_visited = [False]*n
    def dfs(v):
        if rec_visited[v]:
            return False # not a dag
        if not visited[v]:
            visited[v] = True
            rec_visited[v] = True

            for u in g[v]:
                if not dfs(u):
                    return False

            rec_visited[v] = False
            topo_order.append(v)
        return True

    for root in roots:
        if not dfs(root):
            return False
    topo_order.reverse()
    return topo_order
