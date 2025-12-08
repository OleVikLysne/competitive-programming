import sys
import math


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


points = [tuple(map(int, line.split(","))) for line in sys.stdin]
n = len(points)

edges = []
for i in range(n):
    for j in range(i+1, n):
        edges.append((i, j, math.dist(points[i], points[j])))


edges.sort(key=lambda x: x[2], reverse=True)
selected = 0
uf = UnionFind(n)

while selected < n - 2:
    u, v, w = edges.pop()
    if uf.union(u, v):
        selected += 1

while True:
    u, v, w = edges.pop()
    if uf.union(u, v):
        print(points[u][0]*points[v][0])
        break
