import sys; input = sys.stdin.readline
from collections import deque

RIGHT = (0, 1)  # 0
UP = (-1, 0)    # 1
LEFT = (0, -1)  # 2
DOWN = (1, 0)   # 3
DIRECTIONS = (RIGHT, UP, LEFT, DOWN)
DIR_INDICES = (0, 1, 2, 3)


def search(i, j, dir, steps):
    di, dj = DIRECTIONS[dir]
    i += di
    j += dj
    while grid[i][j] != "#":
        update = False
        if res[i][j] == -1:
            res[i][j] = steps
            update = True
        
        if grid[i][j] == ".":
            if update:
                yield i, j, -1
            return
        if update:
            for k in ((dir + 1) % 4, (dir + 3) % 4):
                x = i + DIRECTIONS[k][0]
                y = j + DIRECTIONS[k][1]
                if grid[x][y] == "#":
                    yield i, j, (k + 2) % 4
        i += di
        j += dj


cols, rows = map(int, input().split())
grid = [[char for char in input().rstrip()] for _ in range(rows)]
res = [[-1] * cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "M":
            start = (i, j)
            break
    else:
        continue
    break


i, j = start
res[i][j] = 0
q = deque([(i, j, -1, 0)])
while q:
    i, j, dir, s = q.popleft()
    if dir == -1:
        possible_indices = DIR_INDICES
    else:
        possible_indices = (dir,)
    for k in possible_indices:
        for x, y, dir in search(i, j, k, s + 1):
            q.append((x, y, dir, s + 1))

for row in res:
    print(" ".join(str(x) for x in row))
