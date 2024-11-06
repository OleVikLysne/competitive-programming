

###########
# KRUSKAL #
###########

class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x] += 1
        else:
            self.parent[x] = y
            self.rank[y] += 1


# edges are on the form (u, v, w) where w is a weight
def kruskal(edges: list[tuple[int, int, int]], num_nodes):
    edges.sort(key=lambda x: x[2], reverse=True)
    selected_edges = []
    uf = UnionFind(num_nodes)
    tree_sum = 0

    while len(selected_edges) < num_nodes - 1:
        u, v, w = edges.pop()
        x = uf.find(u)
        y = uf.find(v)
        if x != y:
            selected_edges.append((u, v, w))
            tree_sum += w
            uf.union(x, y)

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
