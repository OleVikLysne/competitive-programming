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


n, m = map(int, input().split())
uf = UnionFind(n+1)
spare_edges = []
for _ in range(m):
    u, v = map(int, input().split())
    if not uf.union(u, v):
        spare_edges.append((u, v))

components = []
for v in range(1, n+1):
    if uf.parent[v] == -1:
        components.append(v)

k = len(components)-1

if k > len(spare_edges):
    print("Nej")
else:
    print("Ja")
    print(k)
    for i in range(k):
        u1, v1 = spare_edges[i]
        u2, v2 = components[i], components[i+1]
        print(u1, v1, u2, v2)
