import sys; input=sys.stdin.readline; print=sys.stdout.write

class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.size = [0] * n

    def find(self, i):
        j = i
        while self.parent[j] != j:
            j = self.parent[j]
        while (k := self.parent[i]) != i:
            self.parent[i] = j
            i = k
        return j

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.size[x] > self.size[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]


def kruskal(edges: list[tuple[int, int, int]], n):
    edges.sort(key=lambda x: x[2])
    selected_edges = 0
    uf = UnionFind(n)
    g = [[] for _ in range(n)]

    while selected_edges < n - 1:
        u, v, w = edges.pop()
        x = uf.find(u)
        y = uf.find(v)
        if x != y:
            uf.union(x, y)
            selected_edges += 1
            g[u].append((v, w))
            g[v].append((u, w))

    return g


INF = 2**30
n, m, q = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u-1, v-1, w))

g = kruskal(edges, n)

parent = [(-1, -1)]*n
depth = [-1]*n
depth[0] = 0
stack = [0]
while stack:
    v = stack.pop()
    for u, w in g[v]:
        if depth[u] != -1: continue
        depth[u] = depth[v] + 1
        parent[u] = (v, w)
        stack.append(u)

x = 0
for _ in range(q):
    u, v, h = map(lambda a: int(a) ^ x, input().split())
    u -= 1
    v -= 1
    d = INF
    while u != v:
        if depth[v] < depth[u]:
            u, v = v, u
        v, w = parent[v]
        d = min(d, w)
        if d < h:
            print("Neibb ")
            break
    else:
        print("Jebb ")
        x += 1
