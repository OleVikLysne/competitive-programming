import io, os
Ø = io.BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: next(Ø)

class UnionFind:
    def __init__(self, n):
        self.parent = [-1]*n
        self.size = [1]*n

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


def anc(v: int, k: int):
    i = k.bit_length()-1
    cost = 0
    while k:
        if k & 1 << i:
            cost = max(cost, anc_cost[i][v])
            v = anc_matrix[i][v]
        k &= (1 << i) - 1
        i -= 1
    return v, cost


def lca_max_cost(u: int, v: int):
    if depth[v] > depth[u]:
        u, v = v, u
    u, cost = anc(u, depth[u]-depth[v])
    if u == v:
        return cost

    log_d = (depth[v]-1).bit_length()
    for i in range(log_d-1, -1, -1):
        if anc_matrix[i][u] != anc_matrix[i][v]:
            cost = max(cost, anc_cost[i][u], anc_cost[i][v])
            u = anc_matrix[i][u]
            v = anc_matrix[i][v]
    cost = max(cost, anc_cost[0][u], anc_cost[0][v])
    return cost


def build_anc_matrix(g: list[list[int]], root=0):
    n = len(g)
    log_n = (n-1).bit_length()
    depth = [-1]*n
    depth[root] = 0
    anc_matrix = [[-1]*n for _ in range(log_n)]
    anc_cost = [[-1]*n for _ in range(log_n)]

    stack = [root]
    while stack:
        v = stack.pop()
        for u, w in g[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                anc_matrix[0][u] = v
                anc_cost[0][u] = w
                stack.append(u)

    for i in range(1, log_n):
        for j in range(n):
            anc_matrix[i][j] = anc_matrix[i-1][anc_matrix[i-1][j]]
            anc_cost[i][j] = max(
                anc_cost[i-1][j],
                anc_cost[i-1][anc_matrix[i-1][j]]
            )

    return depth, anc_matrix, anc_cost

n, m, q = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

edges.sort(key=lambda x: x[2], reverse=True)
uf = UnionFind(n)
g = [[] for _ in range(n)]
c = 0
while c < n - 1:
    u, v, w = edges.pop()
    u -= 1
    v -= 1
    if uf.union(u, v):
        g[u].append((v, w))
        g[v].append((u, w))
        c += 1

depth, anc_matrix, anc_cost = build_anc_matrix(g)
res = [0]*q
for i in range(q):
    u, v, f, k, l = map(int, input().split())
    u -= 1
    v -= 1
    cost = lca_max_cost(u, v)
    j = max(0, -(-(cost-l)//k))
    res[i] = max(0, f-j)

print("\n".join(map(str, res)))
