import sys; input=sys.stdin.readline
sys.setrecursionlimit(2**30)

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

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)


sccs = tarjan(g)
k = len(sccs)
g, node_to_comp = condense_graph(g, sccs)
weight = [0]*k
for i in range(n):
    weight[node_to_comp[i]] += 1


mem = [-1]*n
def solve(v):
    if mem[v] != -1:
        return mem[v]
    res = weight[v]
    for u in g[v]:
        res = max(res, weight[v] + solve(u))
    mem[v] = res
    return res

start = 0
best = 0
for v in range(k):
    x = solve(v)
    if x > best:
        best = x
        start = v

v = start
path = [x+1 for x in sccs[v]]
while g[v]:
    v = max(g[v], key=solve)
    path.extend(x+1 for x in sccs[v])
print(len(path))
print(*path)
print(node_to_comp.index(start) + 1)
