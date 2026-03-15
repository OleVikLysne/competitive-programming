from sys import stdin, stdout
import heapq


def dijkstra(s):
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        _, u = heapq.heappop(pq)
        for (v, w) in G[u]:
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                heapq.heappush(pq, (dist[v], v))

    return dist

while True:
    n, m, q, s = map(int, stdin.readline().split())
    if [n, m, q, s] == [0, 0, 0 ,0]:
        break
    G = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, stdin.readline().split())
        G[u].append((v, w))

    dist = dijkstra(s)

    for _ in range(q):
        v = int(stdin.readline())
        d = dist[v]
        if d == float("inf"):
            stdout.write("Impossible\n")
        else:
            stdout.write(str(d)+"\n")