# 261 / 273 cases

import sys; input = sys.stdin.readline
import heapq

w, h, n = map(int, input().split())

def manhattan_dist(i, j, x, y):
    return abs(i - x) + abs(j - y)


board = tuple([0] * w for _ in range(h))
leaks = []
for _ in range(n):
    a, b = map(int, input().split())
    x = h - b
    y = a - 1
    leaks.append((x, y))

reachable = []
unreachable = []
for i in range(h):
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
            g = unreachable.pop()
            d = steps - manhattan_dist(i, j, *g)
            if d <= 0:
                unreachable.append(g)
                break
            board[i][j] += d
            heapq.heappush(reachable, g[1])

    reachable.clear()
    unreachable.clear()

for i in range(h-2, -1, -1):
    board[i][0] += board[i+1][0]
for j in range(1, w):
    board[h-1][j] += board[h-1][j-1]
    
for i in range(h-2, -1, -1):
    for j in range(1, w):
        board[i][j] += min(
            board[i+1][j],
            board[i][j-1]
        )

print(board[0][w - 1])
