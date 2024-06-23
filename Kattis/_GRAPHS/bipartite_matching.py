n: int = ...
weight_matrix: list[list[int]] = ...
g = ...
node_count = 2*n+2
source = 2*n
sink = 2*n+1
mappings = [0]*n



def dfs(v, flow):
    visited[v] = True
    if v == sink or flow == 0:
        return flow
    for u in g[v]:
        cap = weight_matrix[v][u]
        if cap == 0 or visited[u]:
            continue
        pushed_flow = dfs(u, min(flow, cap))
        if pushed_flow != 0:
            weight_matrix[v][u] -= pushed_flow
            weight_matrix[u][v] += pushed_flow
            if v < n:
                mappings[v] = u % n
            return pushed_flow

    return 0


total_flow = 0
while True:
    visited = [False for _ in range(node_count)]
    flow = dfs(source, float("inf"))
    total_flow += flow
    if flow == 0 or flow == float("inf"):
        break
