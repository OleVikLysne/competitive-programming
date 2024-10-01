def tarjan_SCC(g: list[list[int]]):
    n = len(g)

    on_stack = [False]*n
    low_link = [-1]*n
    index = [-1]*n
    idx = 0
    stack = []
    sccs = []
    def dfs(v):
        nonlocal on_stack, low_link, index, idx, stack, sccs
        low_link[v] = index[v] = idx
        idx += 1
        stack.append(v)
        on_stack[v] = True

        for u in g[v]:
            if low_link[u] == -1:
                dfs(u)
                low_link[v] = min(low_link[v], low_link[u])
            elif on_stack[u]:
                low_link[v] = min(low_link[v], low_link[u])
        
        if low_link[v] == index[v]:
            scc = []
            while True:
                u = stack.pop()
                on_stack[u] = False
                scc.append(u)
                if u == v:
                    break
            sccs.append(scc)
    
    for v in range(n):
        if index[v] == -1:
            dfs(v)
    return sccs