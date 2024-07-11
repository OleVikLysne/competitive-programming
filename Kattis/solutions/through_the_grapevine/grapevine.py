from sys import stdin, stdout

n, m, d = map(int, stdin.readline().split())
idx_map = {}
T = [0]*n
g = [[] for _ in range(n)]
for _ in range(n):
    p, t = stdin.readline().split()
    i = len(idx_map)
    idx_map[p] = i
    T[i] = int(t)

for _ in range(m):
    p1, p2 = stdin.readline().split()
    i, j = idx_map[p1], idx_map[p2]
    g[i].append(j)
    g[j].append(i)

source = idx_map[stdin.readline().rstrip()]

nodes = {source}
in_deg = [0]*n
in_deg[source] = float("inf")
s = 0
for _ in range(d):
    for v in nodes.copy():
        if in_deg[v] >= T[v]:
            nodes.remove(v)
            for u in g[v]:
                if in_deg[u] == 0:
                    s += 1
                    nodes.add(u)
                in_deg[u] += 1

stdout.write(str(s))