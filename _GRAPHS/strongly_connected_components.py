

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



##########
# TARJAN #
##########

def tarjan(g: list[list[int]]):
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



def condense_graph(g: list[set[int]], sccs: list[list[int]]):
    """
        Condense the graph such that every SCC is represented by just one node.
        "node_to_rep" provides a mapping from the original vertex index to its
        "representative" node.

        Modifies the graph in-place.
    """
    n = len(g)
    node_to_rep = [-1]*n

    for scc in sccs:
        rep = scc[0]
        for v in scc:
            node_to_rep[v] = rep

    # add all edges leaving the SCC as out-edges from component rep
    for scc in sccs:
        if len(scc) == 1:
            continue
        rep = node_to_rep[scc[0]]
        for v in scc:
            for u in g[v]:
                if node_to_rep[u] != rep and u != rep:
                    g[rep].add(u)


    # add edges entering the SCC as in-edges for the rep
    for i in range(n):
        if node_to_rep[i] != i:
            g[i].clear()
            continue
        for j in g[i].copy():
            rep = node_to_rep[j]
            if j != rep:
                g[i].remove(j)
            if i != rep:
                g[i].add(rep)

    return g, node_to_rep