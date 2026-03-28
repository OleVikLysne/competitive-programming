capacity: list[list[int]] = ... # contains the initial edge capacities
g: list[list[int]] = ... # undirected and unweighted version of the graph
source: int = ...
sink: int = ...


INF = float("inf")

def push_flow(source, sink, g, capacity):
    n = len(g)
    stack = [(source, INF)]
    #queue = deque([(source, INF)])
    pred = [-1]*n
    pred[source] = source
    while stack:
        v, flow = stack.pop()
        if v == sink:
            break
        for u in g[v]:
            if pred[u] != -1:
                continue
            if capacity[v][u] > 0:
                stack.append((u, min(flow, capacity[v][u])))
                pred[u] = v
    else:
        return 0

    u = sink
    while u != source:
        v = pred[u]
        capacity[v][u] -= flow
        capacity[u][v] += flow
        u = v
    return flow


def ford_fulkerson(source, sink, g, capacity):
    total_flow = 0
    while True:
        flow = push_flow(source, sink, g, capacity)
        total_flow += flow
        if flow == INF or flow == 0:
            break
    return total_flow
