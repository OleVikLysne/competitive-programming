import sys; input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x] += 1
        else:
            self.parent[x] = y
            self.rank[y] += 1

def valid_moves(i, j):
    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if 0 <= x < rows and 0 <= y < cols:
            yield x, y

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def idx(i, j):
    return i*cols+j

cols, rows, q = map(int, input().split())
grid = [[0] * cols for _ in range(rows)]
arr = []
for _ in range(q):
    y1, x1, y2, x2 = map(lambda x: int(x)-1, input().split())
    dx, dy = sign(x2 - x1), sign(y2 - y1)
    if dx == dy == 0:
        dx = 1
    x2 += dx
    y2 += dy
    arr.append((x1, y1, x2, y2))
    while x1 != x2 or y1 != y2:
        grid[x1][y1] += 1
        x1 += dx
        y1 += dy

uf = UnionFind(rows*cols)

visited = [[False]*cols for _ in range(rows)]
def search(i, j):
    visited[i][j] = True
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        for x, y in valid_moves(i, j):
            if visited[x][y] or grid[x][y] != 0: continue
            uf.union(idx(i, j), idx(x, y))
            visited[x][y] = True
            stack.append((x, y))

regions = 0
for i in range(rows):
    for j in range(cols):
        if not visited[i][j] and grid[i][j] == 0:
            regions += 1
            search(i, j)

res = [-1]*q
for z in range(q-1, 0, -1):
    res[z] = regions
    x1, y1, x2, y2 = arr[z]
    dx, dy = sign(x2 - x1), sign(y2 - y1)
    while x1 != x2 or y1 != y2:
        grid[x1][y1] -= 1
        if grid[x1][y1] == 0:
            neighbours = list(valid_moves(x1, y1))
            for k in range(len(neighbours)):
                i, j = neighbours[k]
                if grid[i][j] != 0:
                    continue
                uf.union(idx(x1, y1), idx(i, j))
                p1 = uf.find(idx(i, j))
                for l in range(k+1, len(neighbours)):
                    a, b = neighbours[l]
                    if grid[a][b] != 0:
                        continue
                    p2 = uf.find(idx(a, b))
                    if p1 != p2:
                        uf.union(p1, p2)
                        p1 = uf.find(p1)
                        regions -= 1
                break
            else:
                regions += 1
        x1 += dx
        y1 += dy
res[0] = regions
print(*res)
