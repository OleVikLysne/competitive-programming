import sys; input=sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x] += 1
        else:
            self.parent[x] = y
            self.rank[y] += 1


def kruskal(sec_edges, insec_edges, n, p, insec):
    sec_edges.sort(key=lambda x: x[2])
    insec_edges.sort(key=lambda x: x[2])
    
    edge_count = 0
    uf = UnionFind(n)
    tree_sum = 0
    for u, v, w in sec_edges:
        if edge_count == n - 1:
            break
        x = uf.find(u)
        y = uf.find(v)
        if x != y:
            edge_count += 1
            tree_sum += w
            uf.union(x, y)

    available = [True]*n
    for u, v, w in insec_edges:
        if edge_count == n - 1:
            break
        x = uf.find(u)
        y = uf.find(v)
        if x != y:
            if n != p:
                if not available[u] or not available[v]:
                    continue
                if insec[u] and insec[v]:
                    continue
                if insec[u]:
                    available[u] = False
                elif insec[v]:
                    available[v] = False
            edge_count += 1
            tree_sum += w
            uf.union(x, y)

    return f"{tree_sum} " if edge_count == n - 1 else "impossible "

for line in sys.stdin:
    n, m, p = map(int, line.split())
    insec = [False]*n
    for x in map(int, input().split()):
        insec[x-1] = True
    sec_edges = []
    insec_edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if insec[u] or insec[v]:
            insec_edges.append((u, v, w))
        else:
            sec_edges.append((u, v, w))
    sys.stdout.write(kruskal(sec_edges, insec_edges, n, p, insec))
