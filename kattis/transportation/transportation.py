import sys; input = sys.stdin.readline
n, r, f, t = map(int, input().split())
INF = float("inf")

def dfs(v, flow, visited):
    visited[v] = True
    if v == sink:
        return flow
    for u, cap in enumerate(weight_matrix[v]):
        if cap == 0 or visited[u]:
            continue
        res = dfs(u, min(flow, cap), visited)
        if res != 0:
            weight_matrix[v][u] -= res
            weight_matrix[u][v] += res
            return res

    return 0

def ford_fulkerson(source):
    total_flow = 0
    while True:
        visited = [False for _ in range(node_count)]
        flow = dfs(source, INF, visited)
        total_flow += flow
        if flow == INF or flow == 0:
            break

    return total_flow


m = {}
mat = [m.setdefault(x, len(m)) for x in input().split()]
fac = [m.setdefault(x, len(m)) for x in input().split()]

node_count = n + 2 * t + 2
source = node_count - 2
sink = node_count - 1
weight_matrix = [[0]*node_count for _ in range(node_count)]

for i in range(n, n+t):
    i2 = i+t
    weight_matrix[i][i2] = 1
    l = [m.setdefault(x, len(m)) for x in input().split()[1:]]
    for x in l:
        if x < r: # mat
            weight_matrix[x][i] = 1
        elif x < r+f: # fac
            weight_matrix[i2][x] = 1
        else: # transp
            weight_matrix[i2][x] = 1
            weight_matrix[x][i] = 1

for i in mat:
    weight_matrix[source][i] = 1
for i in fac:
    weight_matrix[i][sink] = 1

print(ford_fulkerson(source))
