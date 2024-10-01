import sys; input=sys.stdin.readline
sys.setrecursionlimit(2**30)
n = int(input())
g = [set() for _ in range(n)]
word_to_idx = {}

inp_list = []
for i in range(n):
    inp = input().split()
    word_to_idx[inp[0]] = i
    inp_list.append(inp)

for i in range(n):
    inp = inp_list[i]
    for k in range(2, len(inp)):
        if (j := word_to_idx.get(inp[k])) is not None and j != i:
            g[i].add(j)


def tarjan(g: list[list[int]]):
    n = len(g)

    on_stack = [False]*n
    lowest = [-1]*n
    index = [-1]*n
    idx = 0
    stack = []
    sccs = []
    def dfs(v):
        nonlocal on_stack, lowest, index, idx, stack, sccs
        lowest[v] = index[v] = idx
        idx += 1
        stack.append(v)
        on_stack[v] = True

        for u in g[v]:
            if lowest[u] == -1:
                dfs(u)
                lowest[v] = min(lowest[v], lowest[u])
            elif on_stack[u]:
                lowest[v] = min(lowest[v], lowest[u])
        
        if lowest[v] == index[v]:
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


sccs = tarjan(g)

def condense_graph(g: list[set[int]], sccs: list[list[int]]):
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

g, node_to_comp = condense_graph(g, sccs)

# identify roots
roots = set(range(n))
for i in range(n):
    for j in g[i]:
        roots.discard(j)

def rev_top_sort(g: list[list[int]], roots: list[int]):
    n = len(g)
    topo_order = []
    visited = [False]*n
    def dfs(v):
        if not visited[v]:
            visited[v] = True
            for u in g[v]:
                dfs(u)
            topo_order.append(v)
    for root in roots:
        dfs(root)

    return topo_order

rev_top_order = rev_top_sort(g, roots)
descendants = [0]*n
for i in range(n):
    descendants[node_to_comp[i]] |= 1 << i

for v in rev_top_order:
    for u in g[v]:
        descendants[v] |= descendants[u]

count = [-1]*n
def get_count(i):
    v = node_to_comp[i]
    if count[v] == -1:
        count[v] = descendants[v].bit_count()
    return count[v]

print(*(get_count(i) for i in range(n)))