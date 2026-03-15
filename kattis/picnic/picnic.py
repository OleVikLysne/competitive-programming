from sys import stdin, stdout

n = int(stdin.readline())
name_map = {}
g = [[] for _ in range(n)]
w = [0 for _ in range(n)]
root = None
for _ in range(n):
    p1, speed, p2 = stdin.readline().split()
    speed = float(speed)

    if p1 not in name_map:
        name_map[p1] = len(name_map)
    p1 = name_map[p1]
    w[p1] = speed
    if p2 == "CEO":
        root = p1
        continue

    if p2 not in name_map:
        name_map[p2] = len(name_map)
    p2 = name_map[p2]
    g[p2].append(p1)


mem = [(-1, -1.0) for _ in range(n)]
def dfs(node):
    if mem[node] != (-1, -1.0):
        return mem[node]

    skip = [0, 0]
    for v in g[node]:
        a, b = dfs(v)
        skip[0] += a
        skip[1] += b

    include = [0, 0]
    for u in g[node]:
        inc = [1, min(w[u], w[node])]
        for v in g[node]:
            if v == u: continue
            a, b = dfs(v)
            inc[0] += a
            inc[1] += b
        for v in g[u]:
            a, b = dfs(v)
            inc[0] += a
            inc[1] += b

        include = max(include, inc)
    mem[node] = max(include, skip)
    return mem[node]


a, b = dfs(root)
b /= (a)
stdout.write(" ".join((str(a), str(b))))