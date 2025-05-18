

###########
# KRUSKAL #
###########

class UnionFind:
    def __init__(self, n):
        self.parent = [-1]*n
        self.size = [0]*n

    def find(self, i):
        j = i
        while self.parent[j] != -1:
            j = self.parent[j]
        while (k := self.parent[i]) != -1:
            self.parent[i] = j
            i = k
        return j

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True


# edges are on the form (u, v, w) where w is a weight
def kruskal(edges: list[tuple[int, int, int]], n):
    edges.sort(key=lambda x: x[2], reverse=True)
    selected_edges = []
    uf = UnionFind(n)
    tree_sum = 0

    while len(selected_edges) < n - 1:
        u, v, w = edges.pop()
        if uf.union(u, v):
            selected_edges.append((u, v, w))
            tree_sum += w

    return selected_edges, tree_sum




########
# PRIM #
########

import heapq

# prim without edge list (faster, one less element in the pq)
def prim(g: list[list[tuple[int, int]]]):
    n = len(g)
    edges = [(x[1], x[0]) for x in g[0]]
    heapq.heapify(edges)
    visited = [False]*n
    visited[0] = True
    tree_sum = 0
    edge_count = 0
    while edge_count < n - 1:
        w, v = heapq.heappop(edges)
        if visited[v]:
            continue
        visited[v] = True
        tree_sum += w
        edge_count += 1
        for u, w in g[v]:
            if visited[u]:
                continue
            heapq.heappush(edges, (w, u))
    return tree_sum


# prim with returned edge list
def prim(g: list[list[tuple[int, int]]]):
    n = len(g)
    edges = [(x[1], 0, x[0]) for x in g[0]]
    heapq.heapify(edges)
    visited = [False]*n
    visited[0] = True
    tree_sum = 0
    selected_edges = []

    while len(selected_edges) < n - 1:
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
