from sys import stdin
import heapq

num_rows, num_cols = map(int, stdin.readline().split())


def neighbours(i, j):
    for x, y in ( (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)):
        if 0 <= x < num_rows and 0 <= y < num_cols:
            yield x, y

grid = [list(map(int, stdin.readline().split())) for _ in range(num_rows)]
i, j = [int(x)-1 for x in stdin.readline().split()]

visited = set()
q = [(0, -i, -j)]

opt = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
opt[i][j] = grid[i][j]
while q:
    _, i, j = heapq.heappop(q)
    i, j = -i, -j
    if (i, j) in visited: continue
    
    visited.add((i, j))
    for k, l in neighbours(i, j):
        if (k, l) in visited: continue
        if opt[k][l] > max(opt[i][j], grid[k][l]):
            opt[k][l] = max(opt[i][j], grid[k][l])
            heapq.heappush(q, (opt[k][l], -k, -l))

print(sum(sum(-x for x in row) for row in opt))