import sys; input=sys.stdin.readline

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
    total_flow = 0
    step = [-1]*n
    pred = [-1]*n
    for i in range(INF):
        flow = push_flow(source, sink, g, capacity, pred, step, i)
        total_flow += flow
        if flow == INF or flow == 0:
            break
    return total_flow


n, k, H = map(int, input().split())
H += 1
N = n**2*2*H+2
source = N-2
sink = N-1

def idx(i, j, h):
    return i*n+j+h*n**2


grid = [[int(x) for x in input().split()] for _ in range(n)]
capacity = [{} for _ in range(N)]
g = [[] for _ in range(N)]

for _ in range(k):
    i, j = map(int, input().split())
    v = idx(i, j, 0)
    capacity[source][v] = 1
    capacity[v][source] = 0
    g[source].append(v)
    g[v].append(source)

for h in range(H):
    for i in range(n):
        for j in range(n):
            u = idx(i, j, h)
            v = idx(i, j, h+H)
            capacity[u][v] = 1
            capacity[v][u] = 0
            g[u].append(v)
            g[v].append(u)


for h in range(1, H):
    level = int(input())
    for i in range(n):
        for j in range(n):
            u = idx(i, j, h-1+H)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i, j)):
                if 0 <= x < n and 0 <= y < n:
                    v = idx(x, y, h)
                    capacity[u][v] = int(grid[x][y] > level)
                    capacity[v][u] = 0
                    g[u].append(v)
                    g[v].append(u)

for i in range(n):
    for j in range(n):
        u = idx(i, j, H-1+H)
        capacity[u][sink] = 1
        capacity[sink][u] = 0
        g[u].append(sink)
        g[sink].append(u)

print(ford_fulkerson(source, sink, g, capacity))