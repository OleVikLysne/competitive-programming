from collections import deque

node_count: int = ...
weight_matrix: list[list[int]] = ... # contains the initial edge capacities
flow_matrix: list[list[int]] = ... # initialized to all zeros, contains the pushed flow for recovering the edges
g: list[list[int]] # undirected and unweighted version of the graph
source: int = ...
sink: int = ...


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