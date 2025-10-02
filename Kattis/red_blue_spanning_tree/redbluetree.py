import sys; input=sys.stdin.readline

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

def kruskal(edges: list[tuple[int, int, int]], n):
    uf = UnionFind(n)
    tree_sum = 0
    c = 0
    i = 0
    while c < n - 1:
        u, v, w = edges[i]
        if uf.union(u, v):
            tree_sum += w
            c += 1
        i += 1

    return tree_sum

n, m, k = map(int, input().split())
edges = [(0, 0, 0)]*m
for i in range(m):
    c, u, v = input().split()
    u, v = int(u)-1, int(v)-1
    c = 1 if c == "B" else 0
    edges[i] = (u, v, c)

edges.sort(key=lambda x: x[2])
min_b = kruskal(edges, n)
edges.reverse()
max_b = kruskal(edges, n)
print(int(min_b <= k <= max_b))
