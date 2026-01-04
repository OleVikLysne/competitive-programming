import sys; input=sys.stdin.readline
from collections import deque
from copy import deepcopy

DIRECTIONS = (
    (0, 1),
    (1, 0), 
    (0, -1),
    (-1, 0)
)
LOWER = ("a", "b", "c", "d")
SWITCH_MAP = {str(x) : char for x, char in zip(range(1, 5), LOWER)}
def valid_moves(i, j):
    for dx, dy in DIRECTIONS:
        x, y = i + dx, j + dy
        if 0 <= x < rows and 0 <= y < cols and grid[x][y] != "*":
            yield dx, dy

def next_pos(i, j, di, dj, state: dict):
    a = i + di
    b = j + dj
    if grid[a][b] == "#" or state.get((a, b), "a").isupper():
        return i, j
    return a, b

def switch(char, state):
    for key in state:
        val = state[key]
        if val.lower() == char:
            if val.isupper():
                state[key] = val.lower()
            else:
                state[key] = val.upper()

rows, cols = map(int, input().split())
grid = [[c for c in input().rstrip()] for _ in range(rows)]

start = []
state = {}
for i in range(rows):
    for j in range(cols):
        if ord("a") <= ord(grid[i][j].lower()) <= ord("d"):
            state[(i, j)] = grid[i][j]
        elif grid[i][j] == "S":
            start.append((i, j))
        grid[i][j] = grid[i][j].lower()


def get_mem(a, b, q, w, state):
    return frozenset(((a, b), (q, w), frozenset(state.items())))


queue = deque([(*start[0], *start[1], state, 0)])
visited = {get_mem(*start[0], *start[1], state)}
while queue:
    i, j, x, y, state, s = queue.popleft()
    if grid[i][j] == grid[x][y] == "e":
        print(s)
        break
    m1 = set(valid_moves(i, j))
    m2 = set(valid_moves(x, y))
    for d1, d2 in m1.intersection(m2):
        a, b = next_pos(i, j, d1, d2, state)
        q, w = next_pos(x, y, d1, d2, state)
        if (a, b) == (q, w) or ((a, b) == (i, j) and (q, w) == (x, y)): 
            continue
        if grid[a][b] in SWITCH_MAP or grid[q][w] in SWITCH_MAP:
            new_state = deepcopy(state)
        else:
            new_state = state

        if (a, b) != (i, j):
            if (char := SWITCH_MAP.get(grid[a][b])) is not None:
                if char == grid[q][w]:
                    continue
                switch(char, new_state)
        if (q, w) != (x, y):
            if (char := SWITCH_MAP.get(grid[q][w])) is not None:
                if char == grid[a][b]:
                    continue
                switch(char, new_state)

        tup = get_mem(a, b, q, w, new_state)
        if tup in visited:
            continue
        visited.add(tup)
        queue.append((a, b, q, w, new_state, s+1))