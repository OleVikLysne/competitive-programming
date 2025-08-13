import sys; input = sys.stdin.readline
from collections import deque

DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]


def valid(x, y):
    return 0 <= x < n and 0 <= y < m


def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1


def creeper_move(pi, pj, ci, cj):
    opts = [(pi - ci, 0), (0, pj - cj)]
    opts.sort(key=lambda x: max(abs(a) for a in x), reverse=True)
    for dx, dy in opts:
        dx, dy = sign(dx), sign(dy)
        x, y = ci + dx, cj + dy
        if valid(x, y) and grid[x][y] != 1:
            return x, y
    return ci, cj


n, m, e = map(int, input().split())
grid = [[0] * m for _ in range(n)]
start = end = creep = (0, 0)
for i in range(n):
    for j, c in enumerate(input().rstrip()):
        if c == "X":
            grid[i][j] = 1
        elif c == "P":
            start = (i, j)
        elif c == "E":
            end = (i, j)
        elif c == "C":
            creep = (i, j)


q = deque([(*start, *creep, 0)])
tried = {(*start, *creep)}
while q:
    pi, pj, ci, cj, t = q.popleft()
    if (pi, pj) == end:
        print(t)
        break
    nci, ncj = creeper_move(pi, pj, ci, cj)
    for dx, dy in DELTAS:
        x, y = pi + dx, pj + dy
        if (
            not valid(x, y)
            or grid[x][y] == 1
            or (x, y, nci, ncj) in tried
            or (abs(x - nci) <= e and abs(y - ncj) <= e)
        ):
            continue
        tried.add((x, y, nci, ncj))
        q.append((x, y, nci, ncj, t + 1))
else:
    print("you're toast")
