import heapq
import sys

def path_search(s, t, cache):
    paths = 0
    for (v, _) in G[s]:
        if v == t:
            paths+=1
            continue
        if dist[v] < dist[s]:
            if v not in cache:
                paths += path_search(v, t, cache)
            else:
                paths += cache[v]
    cache[s] = paths
    return paths


while True:
    i = sys.stdin.readline()
    if i == "0\n": break
    N, M = [int(x) for x in i.split()]
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = [int(x) for x in sys.stdin.readline().split()]
        G[u-1].append((v-1, w))
        G[v-1].append((u-1, w))

    # dijkstra
    dist = [float("inf") for _ in range(N)]
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        _, u = heapq.heappop(pq)
        for (v, w) in G[u]:
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                heapq.heappush(pq, (dist[v], v))
    sys.stdout.write(str(path_search(0, 1, {}))+"\n")