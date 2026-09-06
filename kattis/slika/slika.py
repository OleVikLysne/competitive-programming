import sys; input=sys.stdin.readline


class FenwickTree2D:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.tree = [[0]*(cols+1) for _ in range(rows+1)]

    def update(self, row: int, col: int, val):
        i = row + 1
        while i <= self.rows:
            j = col + 1
            while j <= self.cols:
                self.tree[i][j] += val
                j += j & -j
            i += i & -i

    def query(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return res

    def sum_region(self, r1, c1, r2, c2):
        return self.query(r2, c2) - self.query(r1-1, c2) - self.query(r2, c1-1) + self.query(r1-1, c1-1)

n, k, m = map(int, input().split())
lines = [input().split() for _ in range(m)]
saves = []
discard = [False]*m
for i in range(m):
    if lines[i][0][0] == "S":
        saves.append(i)
        discard[i] = True

for i in range(m-1, -1, -1):
    if discard[i]: continue
    if lines[i][0][0] == "L":
        k = int(lines[i][1]) - 1
        for j in range(saves[k], i+1):
            discard[j] = True


tree = FenwickTree2D(n, n)
res = [[1]*n for _ in range(n)]
for k in range(m-1, -1, -1):
    if discard[k]: continue
    c, r1, c1, r2, c2 = map(int, lines[k][1:])
    if tree.sum_region(r1, c1, r2, c2) == (r2-r1+1)*(c2-c1+1):
        continue
    for i in range(r1, r2+1):
        for j in range(c1+(i-r1)%2, c2+1, 2):
            if res[i][j] == 1:
                res[i][j] = c
                tree.update(i, j, 1)

print("\n".join(" ".join(map(str, row)) for row in res))