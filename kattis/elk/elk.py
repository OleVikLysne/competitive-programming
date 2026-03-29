import sys; input=sys.stdin.readline
sys.setrecursionlimit(2**30)


n, m, a, b = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

on_stack = [False]*n
lowest = [-1]*n
pre_order = [-1]*n
mark = [False]*n
count = 0
stack = []
def dfs(v, p):
    global count
    lowest[v] = pre_order[v] = count
    count += 1
    stack.append(v)
    on_stack[v] = True
    mark[v] = v == b
    for u in g[v]:
        if u == p: continue
        if lowest[u] == -1:
            dfs(u, v)
            lowest[v] = min(lowest[v], lowest[u])
        elif on_stack[u]:
            lowest[v] = min(lowest[v], lowest[u])
        mark[v] |= mark[u]
    
    if lowest[v] == pre_order[v]:
        while (u := stack.pop()) != v:
            mark[u] |= mark[v]
            on_stack[u] = False

dfs(a, -1)

res = [v for v in range(n) if not mark[v]]
print(len(res))
print("\n".join(map(str, res)))
