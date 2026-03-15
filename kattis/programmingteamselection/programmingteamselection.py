import sys; input=sys.stdin.readline
import bisect


def solve(i, adj_n, selected, c):
    if c == len(selected):
        return True
    if selected[i]:
        return solve(i+1, adj_n, selected, c)
    for u, v in adj_n[i]:
        if not (selected[u] or selected[v]):
            selected[u] = True
            selected[v] = True
            selected[i] = True
            if solve(i+1, adj_n, selected, c+3):
                return True
            selected[u] = False
            selected[v] = False
            selected[i] = False
    return False


while (m := int(input())) != 0:
    name_to_idx = {}
    g = []
    for _ in range(m):
        p1, p2 = input().split()
        p1 = name_to_idx.setdefault(p1, len(name_to_idx))
        p2 = name_to_idx.setdefault(p2, len(name_to_idx))
        if p1 >= len(g):
            g.append([])
        if p2 >= len(g):
            g.append([])
        g[p1].append(p2)
        g[p2].append(p1)

    n = len(g)
    if n % 3 != 0:
        print("impossible")
        continue
    for i in range(n):
        g[i].sort()
    adj_n = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(g[i])):
            for k in range(j+1, len(g[i])):
                u, v = g[i][j], g[i][k]
                l = bisect.bisect_left(g[u], v)
                if l < len(g[u]) and g[u][l] == v:
                    adj_n[i].append((u, v))

    print("possible" if solve(0, adj_n, [False]*n, 0) else "impossible")
