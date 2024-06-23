from sys import stdin, stdout

def topological_sort(graph, root=0):
    topo_order = []
    visited = [False]*len(graph)

    def dfs(node):
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                dfs(neighbor)
            topo_order.append(node)
    dfs(root)
    topo_order.reverse()
    return topo_order

def rearrange(top_sort):
    i = 0
    n = len(top_sort)
    while i + 1 < n:
        j = i + 1
        if mask[top_sort[i]] == mask[top_sort[j]]:
            i += 1
            continue
        k = i + 2
        while k < n and k not in g[j]:
            if mask[top_sort[k]] == mask[top_sort[i]]:
                top_sort[k], top_sort[j] = top_sort[j], top_sort[k]
                break
            k += 1

        i += 1
            

def count(top_sort):
    k = mask[top_sort[0]]
    c = 0
    for val in top_sort[1:]:
        if mask[val] != k:
            c += 1
            k = mask[val]
    return c


            
t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    mask = [int(x) for x in stdin.readline().split()]
    g = [set() for _ in range(n)]
    roots = set(range(n))
    for _ in range(m):
        i, j = [int(x)-1 for x in stdin.readline().split()]
        g[i].add(j)
        if j in roots:
            roots.remove(j)
    s = 0
    for root in roots:
        top_sort = topological_sort(g, root)
        rearrange(top_sort)
        s += count(top_sort)
    print(s)
