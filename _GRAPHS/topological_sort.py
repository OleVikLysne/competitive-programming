from sys import setrecursionlimit
setrecursionlimit(2**30)

def topological_sort(g: list[list[int]], roots: list[int]):
    if not roots:
        return False

    topo_order = []
    visited = [False]*len(g)
    rec_stack = set()

    def dfs(v):
        if v in rec_stack:
            return False # not a DAG
        if not visited[v]:
            visited[v] = True
            rec_stack.add(v)

            for u in g[v]:
                if not dfs(u):
                    return False
            rec_stack.remove(v)

            topo_order.append(v)
        return True

    for root in roots:
        if not dfs(root):
            return False
    topo_order.reverse()
    return topo_order