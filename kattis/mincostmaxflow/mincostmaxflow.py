import sys; input=sys.stdin.readline
import heapq

INF = 2**60

def min_cost_max_flow(g, s, t):
    n = len(g)
    h = [0]*n

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


n, m , s, t = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, c, w = map(int, input().split())
    g[u].append([v, c, w, len(g[v])])
    g[v].append([u, 0, -w, len(g[u])-1])

print(*min_cost_max_flow(g, s, t))
