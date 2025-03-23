import sys; input = sys.stdin.readline
INF = 1 << 30

n, d = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(1, n):
    g[int(input())].append(i)

max_dist = [-1]*n
max_count = [-1]*n
stack = [0]
while stack:
    v = stack.pop()
    if max_count[v] == -1:
        stack.append(v)
        max_count[v] = 0
        for u in g[v]:
            stack.append(u)
        continue
    g[v].sort(key=lambda x: max_dist[x], reverse=True)
    max_d = INF
    for u in g[v]:
        if max_d + max_dist[u] + 2 >= d:
            max_count[v] += max_count[u]
            max_d = max_dist[u]
        else:
            max_count[v] += max_count[u] - 1
    if max_d + 1 >= d:
        max_count[v] += 1
        max_dist[v] = 0
    else:
        max_dist[v] = max_d + 1
print(max_count[0])
