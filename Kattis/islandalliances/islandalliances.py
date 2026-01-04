import sys; input=sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = [-1]*n

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
        if len(g[x]) < len(g[y]):
            x, y = y, x
        self.parent[y] = x
        for z in g[y]:
            z = self.find(z)
            g[x].add(z)
            g[z].add(x)
        return True

n, m, q = map(int, input().split())
g = [set() for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].add(v)
    g[v].add(u)

uf = UnionFind(n+1)
for _ in range(q):
    u, v = map(int, input().split())
    u = uf.find(u)
    v = uf.find(v)
    if u in g[v]:
        print("REFUSE")
    else:
        uf.union(u, v)
        print("APPROVE")
