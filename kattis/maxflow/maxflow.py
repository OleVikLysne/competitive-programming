import sys; input=sys.stdin.readline
from collections import deque

def bfs():
    q = deque([(source, float("inf"))])
    pred = [-1]*node_count
    pred[source] = -2
    while q:
        v, flow = q.popleft()
        if v == sink:
            break
        for u in g[v]:
            if pred[u] != -1:
                continue
            if weight_matrix[v][u] > 0:
                q.append((u, min(flow, weight_matrix[v][u])))
                pred[u] = v
    else:
        return 0
    v = sink
    while v != source:
        u = pred[v]
        weight_matrix[u][v] -= flow
        weight_matrix[v][u] += flow
        flow_matrix[u][v] += flow
        flow_matrix[v][u] -= flow
        v = u
    return flow


def edmonds_karp():
    total_flow = 0
    while True:
        flow = bfs()
        if flow == float("inf") or flow == 0:
            break
        total_flow += flow
    return total_flow

n, m, source, sink = map(int, input().split())
node_count = n
weight_matrix = [[0 for _ in range(n)] for _ in range(n)]
flow_matrix = [[0 for _ in range(n)] for _ in range(n)]
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    weight_matrix[u][v] = w

flow = edmonds_karp()
l = []
for i in range(n):
    for j in range(n):
        if flow_matrix[i][j] > 0:
            l.append((i, j, flow_matrix[i][j]))

print(n, flow, len(l))
for u, v, w in l:
    print(u, v, w)