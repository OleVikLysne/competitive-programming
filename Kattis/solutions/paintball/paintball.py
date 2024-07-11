from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
node_count = 2*n+2
weight_matrix = [[0 for _ in range(node_count)] for _ in range(node_count)]
g = [[] for _ in range(node_count)]
for _ in range(m):
    a, b = [int(x)-1 for x in stdin.readline().split()]
    weight_matrix[a][b+n] = 1
    weight_matrix[b][a+n] = 1
    g[a].append(b+n)
    g[b].append(a+n)


source = 2*n
sink = 2*n+1
for i in range(n):
    weight_matrix[source][i] = 1
    weight_matrix[i+n][sink] = 1
    g[source].append(i)
    g[i+n].append(sink)



def dfs(v, flow):
    visited[v] = True
    if v == sink:
        return flow
    for u in g[v]:
        cap = weight_matrix[v][u]
        if cap == 0 or visited[u]:
            continue
        pushed_flow = dfs(u, min(flow, cap))
        if pushed_flow != 0:
            weight_matrix[v][u] -= pushed_flow
            weight_matrix[u][v] += pushed_flow
            if v not in g[u]:
                g[u].append(v)
            return pushed_flow
    return 0


total_flow = 0
while True:
    visited = [False for _ in range(node_count)]
    flow = dfs(source, float("inf"))
    total_flow += flow
    if flow == float("inf") or flow == 0:
        break


if total_flow < n:
    stdout.write("Impossible")
else:
    for i in range(n):
        for j in g[i]:
            if weight_matrix[j][i] > 0:
                stdout.write(str((j%n)+1)+"\n")
                continue