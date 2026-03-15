import sys; input=sys.stdin.readline
from collections import deque

n = int(input())
grid = [[c == "O" for c in input()] for _ in range(n)]

state = 0
for i in range(1, n-1):
    for j in range(1, n-1):
        if not grid[i][j]:
            state |= 1 << i*n+j

def get_path(state):
    path = []
    while True:
        state = pred[state]
        if state == -1:
            break
        l = state & 3
        state ^= l
        path.append(l)
    path.reverse()
    return path

DIRS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

DIR_WORD = [
    "east",
    "south",
    "west",
    "north"
]

pred = {state: -1}
q = deque([state])
best = state.bit_count()
while q:
    state = q.popleft()
    for l in range(4):
        di, dj = DIRS[l]
        new_state = 0
        for k in range(n+1, n*(n-1)):
            if not state & 1 << k:
                continue
            i, j = k // n, k % n
            x, y = i+di, j+dj
            if grid[x][y]:
                new_state |= 1 << i*n+j
            elif 0 < x < n-1 and 0 < y < n-1:
                new_state |= 1 << x*n+y
        if new_state not in pred:
            pred[new_state] = state + l
            if not new_state:
                print(*(DIR_WORD[x] for x in get_path(new_state)))
                exit()
            b = new_state.bit_count()
            if b <= best+4:
                q.append(new_state)
            best = min(best, b)