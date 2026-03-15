import sys; input = sys.stdin.readline
from collections import deque

rows, cols = map(int, input().split())
grid = [[char for char in input()] for _ in range(rows)]
visited = [[False]*cols for _ in range(rows)]
visited[0][0] = True
q = deque([(0, 0, 0)])

while q:
    i, j, c = q.popleft()
    if i == rows - 1:
        print(c + 1)
        break
    for x, y in ((i + 1, j), (i - 1, j), (i, (j - 1) % cols), (i, j)):
        if x >= 0 and grid[x][y] != "M":
            y = (y - 1) % cols
            if grid[x][y] != "M" and not visited[x][y]:
                visited[x][y] = True
                q.append((x, y, c + 1))
else:
    print(-1)
