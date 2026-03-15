import sys; input=sys.stdin.readline
from collections import deque

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

n, a, b = map(int, input().split())
P = [0]*n
L = [0]*n
R = [0]*n
for i in range(n):
    l, r, t = map(int, input().split())
    L[i] = l
    R[i] = r
    P[i] = t

uf = UnionFind(n)
q = deque([(0, a, b)])
while q:
    d, u, v = q.popleft()
    if P[u] != P[v]:
        print(d)
        break
    if uf.union(u, v):
        q.append((d+1, L[u], L[v]))
        q.append((d+1, R[u], R[v]))
else:
    print("indistinguishable")