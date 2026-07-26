capacity: list[list[int]] = ... # contains the initial edge capacities
g: list[list[int]] = ... # undirected and unweighted version of the graph
source: int = ...
sink: int = ...


INF = 2**60

def push_flow(source, sink, g, capacity, pred, step, i):
    stack = [(source, INF)]
    #queue = deque([(source, INF)])
    pred[source] = source
    while stack:
        v, flow = stack.pop()
        if v == sink:
            break
        for u in g[v]:
            if step[u] == i or (cap := capacity[v][u]) <= 0:
                continue
            stack.append((u, min(flow, cap)))
            step[u] = i
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
    n = len(g)
    step = [-1]*n
    pred = [-1]*n
    total_flow = 0
    for i in range(INF):
        flow = push_flow(source, sink, g, capacity, pred, step, i)
        total_flow += flow
        if flow == INF or flow == 0:
            break
    return total_flow
