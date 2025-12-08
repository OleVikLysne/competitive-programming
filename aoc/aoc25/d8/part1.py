import sys
import math


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
        self.size[y] = 0
        return True

points = [tuple(map(int, line.split(","))) for line in sys.stdin]
n = len(points)

dists = []
for i in range(n):
    for j in range(i+1, n):
        dists.append((i, j, math.dist(points[i], points[j])))

uf = UnionFind(n)
dists.sort(key=lambda x: x[2])
for i, j, _ in dists[:1000]:
    uf.union(i, j)

s = sorted(uf.size, reverse=True)
a, b, c = s[0], s[1], s[2]
print(a*b*c)
