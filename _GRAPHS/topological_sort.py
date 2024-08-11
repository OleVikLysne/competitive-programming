from sys import setrecursionlimit
setrecursionlimit(2**30)

def topological_sort(g: list[list[int]], roots: list[int]):
    if not roots:
        return False

    n = len(g)
    topo_order = [-1]*n
    visited = [False]*n
    rec_stack = set()
    i = n - 1
    def dfs(v):
        nonlocal i
        if v in rec_stack:
            return False # not a DAG
        if not visited[v]:
            visited[v] = True
            rec_stack.add(v)

            for u in g[v]:
                if not dfs(u):
                    return False
            rec_stack.remove(v)

            topo_order[i] = v
            i -= 1
        return True

    for root in roots:
        if not dfs(root):
            return False
    return topo_order