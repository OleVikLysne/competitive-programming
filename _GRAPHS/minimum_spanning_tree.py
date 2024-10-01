

###########
# KRUSKAL #
###########

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += 1
    else:
        parent[x] = y
        rank[y] += 1


# edges are on the form (u, v, w) where w is a weight
def kruskal(edges: list[tuple[int, int, int]], num_nodes):
    edges.sort(key=lambda x: x[2], reverse=True)
    selected_edges = []
    parent = [x for x in range(num_nodes)]
    rank = [0] * num_nodes
    tree_sum = 0

    while len(selected_edges) < num_nodes - 1:
        u, v, w = edges.pop()
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            selected_edges.append((u, v, w))
            tree_sum += w
            union(parent, rank, x, y)

    return selected_edges, tree_sum




########
# PRIM #
########

import heapq

# prim without edge list (faster, one less element in the pq)
def prim(g: list[list[tuple[int, int]]]):
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


# prim with returned edge list
def prim(g: list[list[tuple[int, int]]]):
    num_nodes = len(g)
    edges = [(x[1], 0, x[0]) for x in g[0]]
    heapq.heapify(edges)
    visited = [False]*num_nodes
    visited[0] = True
    tree_sum = 0
    selected_edges = []

    while len(selected_edges) < num_nodes - 1:
        w, parent, child = heapq.heappop(edges)
        if visited[child]:
            continue
        visited[child] = True
        tree_sum += w
        selected_edges.append((parent, child, w))
        for u, w in g[child]:
            if visited[u]:
                continue
            heapq.heappush(edges, (w, child, u))
    return selected_edges, tree_sum
