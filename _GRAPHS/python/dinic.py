from collections import deque
node_count: int = ...
weight_matrix: list[list[int]] = ... # contains the initial edge capacities
flow_matrix: list[list[int]] = ... # initialized to all zeros, contains the pushed flow for recovering the edges

def bfs(source, sink, level):
    q = deque([source])
    level[source] = 0
    while q:
        v = q.popleft()
        for u in range(node_count):
              cap = weight_matrix[v][u]
              if cap > 0 and level[u] < 0:
                  level[u] = level[v] + 1
                  q.append(u)
    return level[sink] != -1

def dfs(v, flow, sink, ptr, level):
    if v == sink or flow == 0:
        return flow
    
    for u in range(ptr[v], node_count):
        cap = weight_matrix[v][u]
        if level[u] == level[v]+1 and cap > 0:
            pushed_flow = dfs(u, min(flow, cap), sink, ptr, level)
            if pushed_flow > 0:
                weight_matrix[v][u] -= pushed_flow
                weight_matrix[u][v] += pushed_flow
                flow_matrix[v][u] += pushed_flow
                flow_matrix[u][v] -= pushed_flow
                return pushed_flow
        ptr[v] += 1
    return 0

def dinic(source, sink):
    total_flow = 0
    level = [-1]*node_count
    level[source] = 0
    while bfs(source, sink, level):
        ptr = [0]*node_count
        while True:
            flow = dfs(source, float("inf"), sink, ptr, level)
            if flow == 0:
                break
            total_flow += flow
        level = [-1]*node_count
        level[source] = 0
    return total_flow


def get_flow_edges(flow_matrix):
    l = []
    for i in range(node_count):
        for j in range(node_count):
            if flow_matrix[i][j] > 0:
                l.append((i, j, flow_matrix[i][j]))
    return l