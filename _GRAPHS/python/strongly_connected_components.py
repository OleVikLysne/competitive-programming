

############
# KOSARAJU #
############

def kosaraju(g: list[list[int]], rev_g: list[list[int]]) -> list[list[int]]:
    n = len(g)
    visited = [False]*n
    order = []
    sccs = []
    component = [-1]*n
    def dfs(v):
        visited[v] = True
        for u in g[v]:
            if not visited[u]:
                dfs(u)
        order.append(v)

    def rev_dfs(v, root, comp = None):
        if comp is None:
            comp = []
        component[v] = root
        comp.append(v)
        for u in rev_g[v]:
            if component[u] == -1:
                comp = rev_dfs(u, root, comp)
        return comp

    for v in range(n):
        if not visited[v]:
            dfs(v)

    for i in range(len(order)-1, -1, -1):
        v = order[i]
        if component[v] == -1:
            sccs.append(rev_dfs(v, v))
    
    return sccs



##########
# TARJAN #
##########

def tarjan(g: list[list[int]]) -> list[list[int]]:
    n = len(g)

    on_stack = [False]*n
    lowest = [-1]*n
    pre_order = [-1]*n
    count = 0
    stack = []
    sccs = []
    def dfs(v):
        nonlocal count
        lowest[v] = pre_order[v] = count
        count += 1
        stack.append(v)
        on_stack[v] = True

        for u in g[v]:
            if lowest[u] == -1:
                dfs(u)
                lowest[v] = min(lowest[v], lowest[u])
            elif on_stack[u]:
                lowest[v] = min(lowest[v], lowest[u])
        
        if lowest[v] == pre_order[v]:
            scc = []
            while True:
                u = stack.pop()
                on_stack[u] = False
                scc.append(u)
                if u == v:
                    break
            sccs.append(scc)
    
    for v in range(n):
        if pre_order[v] == -1:
            dfs(v)
    return sccs



def condense_graph(g: list[list[int]], sccs: list[list[int]]) -> list[set[int]]:
    """
        Condense the graph such that every SCC is represented by just one node.
        "node_to_comp" provides a mapping from the original vertex index to its
        "representative" in the new graph.
    """
    n = len(g)
    k = len(sccs)
    node_to_comp = [-1]*n
    for i in range(k):
        for v in sccs[i]:
            node_to_comp[v] = i

    new_g = [set() for _ in range(k)]
    for i in range(n):
        v = node_to_comp[i]
        for j in g[i]:
            u = node_to_comp[j]
            if v != u:
                new_g[v].add(u)
    return new_g, node_to_comp