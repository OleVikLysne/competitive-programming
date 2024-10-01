

##########
# TARJAN #
##########

def tarjan(g: list[list[int]]):
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


############
# KOSARAJU #
############

def kosaraju(g: list[list[int]], rev_g: list[list[int]]):
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





def condense_graph(g: list[set[int]], sccs: list[list[int]]):
    """
        Condense the graph such that every SCC is represented by just one node.
        "node_to_comp" provides a mapping from the original vertex index to its
        "representative" node.

        Modifies the graph in-place.
    """
    n = len(g)
    node_to_comp = [x for x in range(n)]

    for scc in sccs:
        root = scc[0]
        for v in scc:
            node_to_comp[v] = root

    # add all edges leaving the SCC as out-edges from component root
    for ssc in sccs:
        if len(ssc) == 1:
            continue
        root = node_to_comp[ssc[0]]
        for v in ssc:
            for u in g[v]:
                if node_to_comp[u] != root and u != root:
                    g[root].add(u)


    # add edges entering the SCC as in-edges for the root
    for i in range(n):
        if node_to_comp[i] != i:
            g[i].clear()
            continue
        for j in g[i].copy():
            root = node_to_comp[j]
            if root != j:
                g[i].remove(j)
            if root != i:
                g[i].add(root)

    return g, node_to_comp