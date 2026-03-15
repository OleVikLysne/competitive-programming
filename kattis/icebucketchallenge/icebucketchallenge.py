import sys; input=sys.stdin.readline
import heapq

rows, cols, d = map(int, input().split())
si, sj = (int(x)-1 for x in input().split())
grid = [[int(x) for x in input().split()] for _ in range(rows)]
res = [[0]*cols for _ in range(rows)]
heap = [(-grid[si][sj], -d, si, sj)]
res[si][sj] = d

while heap:
    h, l, i, j = heapq.heappop(heap)
    l = -l
    if l < res[i][j] or l <= 1:
        continue
    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if 0 <= x < rows and 0 <= y < cols:
            if grid[x][y] < grid[i][j]:
                if res[x][y] < d:
                    res[x][y] = d
                    heapq.heappush(heap, (-grid[x][y], -d, x, y))
            elif grid[x][y] == grid[i][j]:
                if res[x][y] < l-1:
                    res[x][y] = l-1
                    if res[x][y] > 1:
                        heapq.heappush(heap, (-grid[x][y], -(l-1), x, y))

print("\n".join(" ".join(str(x) for x in row) for row in res))