import sys; input=sys.stdin.readline
import heapq


def prim(g: list[tuple[int, int]]):
    num_nodes = len(g)
    edges = [(x[1], x[0]) for x in g[0]]
    heapq.heapify(edges)
    visited = [False]*num_nodes
    visited[0] = True
    tree_sum = 0
    n = 0
    while n < num_nodes - 1:
        w, v = heapq.heappop(edges)
        if visited[v]:
            continue
        visited[v] = True
        tree_sum += w
        n += 1
        for u, w in g[v]:
            if visited[u]:
                continue
            heapq.heappush(edges, (w, u))
    return tree_sum


for _ in range(int(input())):
    m, c = map(int, input().split())
    g = [[] for _ in range(c)]
    for _ in range((c*(c-1)//2)):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))

    if prim(g) + c <= m:
        print("yes")
    else:
        print("no")