n: int = ...
weight_matrix: list[list[int]] = ...
node_count: int = n+2 # depends on the task
source = n # depends on the task
sink = n+1 # depends on the task


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
        flow = dfs(source, float("inf"), visited)
        total_flow += flow
        if flow == float("inf") or flow == 0:
            break

    return total_flow

