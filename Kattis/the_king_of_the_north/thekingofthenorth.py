import sys; input=sys.stdin.readline
from collections import defaultdict

INF = float("inf")

def idx(i, j):
    return i*cols+j
def mid(v):
    return v + rows * cols

rows, cols = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(rows)]
N = rows*cols*2 + 1
sink = N - 1

g = [[] for _ in range(N)]
weight_matrix = [defaultdict(int) for _ in range(N)]
sx, sy = map(int, input().split())

for i in range(rows):
    for j in range(cols):
        v = idx(i, j)
        mid_v = mid(v)
        weight_matrix[v][mid_v] = grid[i][j]
        g[v].append(mid_v)
        g[mid_v].append(v)
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < rows and 0 <= y < cols:
                u = idx(x, y)
                weight_matrix[mid_v][u] = INF
                g[mid_v].append(u)
                g[u].append(mid_v)
source = idx(sx, sy)

for i in range(rows):
    k = mid(idx(i, 0))
    weight_matrix[k][sink] = grid[i][0]
    g[k].append(sink)
    g[sink].append(k)
    k = mid(idx(i, cols-1))
    weight_matrix[k][sink] = grid[i][cols-1]
    g[k].append(sink)
    g[sink].append(k)

for j in range(1, cols-1):
    k = mid(idx(0, j))
    weight_matrix[k][sink] = grid[0][j]
    g[k].append(sink)
    g[sink].append(k)
    k = mid(idx(rows-1, j))
    weight_matrix[k][sink] = grid[rows-1][j]
    g[k].append(sink)
    g[sink].append(k)



def dfs(source, sink):
    stack = [(source, INF)]
    pred = [-1]*N
    while stack:
        v, flow = stack.pop()
        if v == sink:
            break
        for u in g[v]:
            if pred[u] != -1:
                continue
            cap = weight_matrix[v][u]
            if cap > 0:
                stack.append((u, min(flow, cap)))
                pred[u] = v
    else:
        return 0
    u = sink
    while u != source:
        v = pred[v]
        weight_matrix[v][u] -= flow
        weight_matrix[u][v] += flow
        u = v
    return flow


def ford_fulkerson(source, sink):
    total_flow = 0
    while True:
        flow = dfs(source, sink)
        if flow == 0 or flow == INF:
            break
        total_flow += flow
    return total_flow

print(ford_fulkerson(source, sink))