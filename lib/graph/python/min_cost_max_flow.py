import heapq

# An edge in g[v] is on the form [u, capacity, cost, i] where i is the index of the edge in g[u] representing u -> v
def min_cost_max_flow(g: list[list[int, int, int, int]], s: int, t: int):
    INF = 2**60
    n = len(g)

    # bellman ford
    h = [INF]*n
    h[s] = 0
    for _ in range(n-1):
        for v in range(n):
            for u, c, w, _ in g[v]:
                if c == 0: continue
                if h[u] > h[v] + w:
                    h[u] = h[v] + w
    for v in range(n):
        for u, c, w, _ in g[v]:
            if c == 0: continue
            if h[u] > h[v] + w:
                return False # negative cycle

    total_flow = 0
    total_cost = 0
    # dijkstra
    while True:
        dist = [INF]*n
        dist[s] = 0
        heap = [(0, s)]
        pred_node = [-1]*n
        pred_edge = [-1]*n
        while heap:
            d, v = heapq.heappop(heap)
            if dist[v] < d: continue
            for i, (u, c, w, j) in enumerate(g[v]):
                if c == 0: continue
                wp = w + h[v] - h[u]
                if dist[u] > dist[v] + wp:
                    dist[u] = dist[v] + wp
                    pred_node[u] = v
                    pred_edge[u] = i
                    heapq.heappush(heap, (dist[u], u))
        
        if dist[t] == INF:
            break

        # update potentials
        for v in range(n):
            h[v] = min(h[v] + dist[v], INF)

        # find the pushed flow
        pushed_flow = INF
        u = t
        while u != s:
            v = pred_node[u]
            i = pred_edge[u]
            pushed_flow = min(pushed_flow, g[v][i][1])
            u = v

        # push the flow
        u = t
        while u != s:
            v = pred_node[u]
            i = pred_edge[u]
            j = g[v][i][3]
            g[v][i][1] -= pushed_flow
            g[u][j][1] += pushed_flow
            total_cost += pushed_flow * g[v][i][2]
            u = v

        total_flow += pushed_flow

    return total_flow, total_cost
