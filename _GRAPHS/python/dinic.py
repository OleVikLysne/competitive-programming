capacity: list[list[int]] = ... # contains the initial edge capacities
source: int = ...
sink: int = ...


from collections import deque

INF = float("inf")

def bfs(source, sink, level, capacity):
    n = len(capacity)
    q = deque([source])
    level[source] = 0
    while q:
        v = q.popleft()
        for u in range(n):
              cap = capacity[v][u]
              if cap > 0 and level[u] < 0:
                  level[u] = level[v] + 1
                  q.append(u)
    return level[sink] != -1

def dfs(v, flow, sink, ptr, level, capacity):
    if v == sink or flow == 0:
        return flow
    n = len(capacity)
    for u in range(ptr[v], n):
        cap = capacity[v][u]
        if level[u] == level[v]+1 and cap > 0:
            pushed_flow = dfs(u, min(flow, cap), sink, ptr, level, capacity)
            if pushed_flow > 0:
                capacity[v][u] -= pushed_flow
                capacity[u][v] += pushed_flow
                return pushed_flow
        ptr[v] += 1
    return 0

def dinic(source, sink, capacity):
    n = len(capacity)
    total_flow = 0
    level = [-1]*n
    level[source] = 0
    while bfs(source, sink, level, capacity):
        ptr = [0]*n
        while True:
            flow = dfs(source, INF, sink, ptr, level, capacity)
            if flow == 0:
                break
            total_flow += flow
        level = [-1]*n
        level[source] = 0
    return total_flow
