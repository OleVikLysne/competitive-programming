from sys import stdin, stdout
from collections import deque

# 35 #
# 42 *
# 64 @

def valid_moves(i, j, grid):
    for x, y in ( (i+1, j), (i-1, j), (i, j+1), (i, j-1) ):
        if 0 <= x < h and 0 <= y < w and grid[x][y] != 35 and grid[x][y] != 42:
            yield (x, y)


def fire_step(fire, grid):
    new_fires = []
    for pos in fire:
        for x, y in valid_moves(*pos, grid):
            grid[x][y] = 42
            new_fires.append((x, y))
    return new_fires


def bfs(start_pos, fires, grid):    
    q = deque([(start_pos, 0)])
    fire_steps = 0
    visited = set([start_pos])
    while q:
        (i, j), steps = q.popleft()
        if i == 0 or i == h-1 or j == w-1 or j == 0:
            return steps+1
        
        if steps == fire_steps:
            fires = fire_step(fires, grid)
            fire_steps += 1
        
        for x, y in valid_moves(i, j, grid):
            if (x, y) in visited: continue
            visited.add((x, y))
            q.append(((x, y), steps+1))

    return None

n = int(stdin.readline())
for _ in range(n):
    w, h = map(int, stdin.readline().split())
    grid = [[ord(x) for x in stdin.readline()] for _ in range(h)]
    fires = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 42:
                fires.append((i, j))
            elif grid[i][j] == 64:
                start_pos = (i, j)
    
    res = bfs(start_pos, fires, grid)
    if res is None:
        stdout.write("IMPOSSIBLE\n")
    else:
        stdout.write(str(res)+"\n")