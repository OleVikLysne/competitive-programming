# 261 / 273 cases

import sys

input = sys.stdin.readline
import heapq

w, h, n = map(int, input().split())


def invalid(x, y):
    return x < 0 or x >= h or y < 0 or y >= w


def manhattan_dist(i, j, x, y):
    return abs(i - x) + abs(j - y)


def quarter_ring(y):
    x = h - 1
    dist = y - w + 1
    if dist > 0:
        y -= dist
        x -= dist

    yield x, y

    for _ in range(y):
        x -= 1
        y -= 1
        if invalid(x, y):
            return
        yield x, y


board = tuple([0] * w for _ in range(h))
leaks = []
for _ in range(n):
    a, b = map(int, input().split())
    x = h - b
    y = a - 1
    leaks.append((x, y))

for i in range(h):
    reachable = []
    unreachable = []
    steps = h - i
    for x, y in leaks:
        d = steps - (abs(i - x) + y)
        if d > 0:
            board[i][0] += d
            reachable.append(y)
        elif manhattan_dist(x, y, i, w) < w + h - i:
            unreachable.append((x, y))
    heapq.heapify(reachable)
    unreachable.sort(key=lambda x: abs(i - x[0]) + x[1], reverse=True)
    for j in range(1, w):
        while reachable and reachable[0] < j:
            heapq.heappop(reachable)
        board[i][j] = board[i][j - 1] + len(reachable) * 2
        steps = abs(h - i) + j
        while unreachable:
            x, y = unreachable[-1]
            d = steps - manhattan_dist(i, j, x, y)
            if d <= 0:
                break
            board[i][j] += d
            heapq.heappush(reachable, y)
            unreachable.pop()


for step in range(1, w + h - 1):
    for x, y in quarter_ring(step):
        val = 1 << 62
        if not invalid(x + 1, y) and board[x + 1][y] < val:
            val = board[x + 1][y]
        if not invalid(x, y - 1) and board[x][y - 1] < val:
            val = board[x][y - 1]
        board[x][y] += val
print(board[0][w - 1])
