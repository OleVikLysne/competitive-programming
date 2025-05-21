g: list[list[tuple[int, float | int]]] = ...

INF = float("inf")


from collections import deque
def SPFA(g, s):
    n = len(g)
    dist = [INF]*n
    pred = [-1]*n
    in_queue = [False]*n
    visits = [0]*n
    dist[s] = 0

    q = deque([s])
    while q:
        v = q.popleft()
        if visits[v] >= n:
            break # negative cycle
        in_queue[v] = False
        visits[v] += 1
        for u, w in g[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                pred[u] = v
                if not in_queue[u]:
                    in_queue[u] = True
                    q.append(u)
    return dist, pred

def bellman_ford(g, s):
    n = len(g)
    dist = [INF]*n
    pred = [-1]*n
    dist[s] = 0
    for _ in range(n-1):
        for parent in range(n):
            for child, w in g[parent]:
                if dist[child] > dist[parent] + w:
                    dist[child] = dist[parent] + w
                    pred[child] = parent

    for parent in range(n):
        for child, w in g[parent]:
            if dist[child] > dist[parent] + w:
                return True # negative cycle
    return dist, pred


def floyd_warshall(dist: list[list[int]]):
    n = len(dist)
    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for j in range(n):
            for i in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(n):
        for j in range(n):
            if dist[i][j] == -INF:
                continue
            for k in range(n):
                if dist[i][k] < INF and dist[k][j] < INF and dist[k][k] < 0:
                    dist[i][j] == -INF
    return dist
