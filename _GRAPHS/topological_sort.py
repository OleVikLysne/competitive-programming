from sys import setrecursionlimit
setrecursionlimit(2**30)

def topological_sort(g: list[list[int]], roots: list[int]):
    if not roots:
        return False

    n = len(g)
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