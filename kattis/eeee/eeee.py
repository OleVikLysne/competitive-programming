import sys; input=sys.stdin.readline
sys.setrecursionlimit(2**30)
n = int(input())
g = [set() for _ in range(n)]
word_to_idx = {}

inp_list = []
for i in range(n):
    word, _, *inp = input().split()
    word_to_idx[word] = i
    inp_list.append(inp)

for i in range(n):
    for word in inp_list[i]:
        if (j := word_to_idx.get(word)) is not None and j != i:
            g[i].add(j)


def tarjan(g: list[list[int]]):
    n = len(g)

    on_stack = [False]*n
    lowest = [-1]*n
    pre_order = [-1]*n
    idx = 0
    stack = []
    sccs = []
    def dfs(v):
        nonlocal idx
        lowest[v] = pre_order[v] = idx
        idx += 1
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
    for ssc in sccs:
        if len(ssc) == 1:
            continue
        rep = node_to_rep[ssc[0]]
        for v in ssc:
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

sccs = tarjan(g)
g, node_to_rep = condense_graph(g, sccs)

descendants = [0]*n
for i in range(n):
    descendants[node_to_rep[i]] |= 1 << i


visited = [False]*n
def search(v):
    visited[v] = True
    for u in g[v]:
        if not visited[u]:
            search(u)
        descendants[v] |= descendants[u]

for v in range(n):
    if not visited[v]:
        search(v)

print(*(descendants[node_to_rep[i]].bit_count() for i in range(n)))