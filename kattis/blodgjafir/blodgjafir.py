import sys; input = sys.stdin.readline

INF = 2**60


def push_flow(source, sink, g, capacity):
    n = len(g)
    stack = [(source, INF)]
    pred = [-1]*n
    pred[source] = source
    while stack:
        v, flow = stack.pop()
        if v == sink:
            break
        for u in g[v]:
            if pred[u] != -1 or (cap := capacity[v][u]) <= 0:
                continue
            stack.append((u, min(flow, cap)))
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


C = {
    "O": ["o", "a", "b", "ab"],
    "A": ["a", "ab"],
    "B": ["b", "ab"],
    "AB": ["ab"],
    "O+": ["o+", "a+", "b+", "ab+"],
    "O-": ["o+", "o-", "a+", "a-", "b+", "b-", "ab+", "ab-"],
    "A+": ["a+", "ab+"],
    "A-": ["a+", "a-", "ab+", "ab-"],
    "B+": ["b+", "ab+"],
    "B-": ["b+", "b-", "ab+", "ab-"],
    "AB+": ["ab+"],
    "AB-": ["ab+", "ab-"],
}

idx = {}
for i, x in enumerate(C):
    idx[x] = i
    idx[x.lower()] = i + len(C)

N = len(C) * 2 + 2
capacity = [[0]*N for _ in range(N)]

for x in C:
    i = idx[x]
    for y in C:
        capacity[i][idx[y.lower()]] = INF

source = N-2
sink = N-1
g = [[] for _ in range(N)]
for x, neigh in C.items():
    v = idx[x]
    u = idx[x.lower()]
    g[v].append(source)
    g[source].append(v)
    g[sink].append(u)
    g[u].append(sink)
    for u in neigh:
        u = idx[u]
        g[v].append(u)
        g[u].append(v)

n = int(input())
for d in input().split():
    d = idx[d]
    capacity[source][d] += 1

m = int(input())
for r in input().split():
    r = idx[r.lower()]
    capacity[r][sink] += 1

flow = ford_fulkerson(source, sink, g, capacity)
print("Jebb" if flow == m else "Neibb")