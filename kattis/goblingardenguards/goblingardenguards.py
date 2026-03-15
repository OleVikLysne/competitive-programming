import sys; input = sys.stdin.readline
import math

MAX = 10_001

class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.count = 1
        self.next = None

n = int(input())
goblins = [tuple(map(int, input().split())) for _ in range(n)]
goblins.sort(key=lambda x: x[1])
m = int(input())
sprinklers = [tuple(map(int, input().split())) for _ in range(m)]

head = [Node(-1000) for _ in range(MAX)]
tail = [x for x in head]
for x, y in goblins:
    node = tail[x]
    if y == node.val:
        node.count += 1
        continue
    tail[x] = Node(y, parent=node)
    node.next = tail[x]

count = 0
for xval, yval, r in sprinklers:
    for x in range(max(xval - r, 0), min(xval + r + 1, MAX)):
        y = int(math.sqrt(r**2 - (xval - x)**2))
        y1 = max(yval - y, 0)
        y2 = min(yval + y, MAX - 1)
        lower = head[x]
        while lower is not None and lower.val < y1:
            lower = lower.next

        if lower is None or lower.val < y1:
            continue
        upper = lower
        while upper is not None and upper.val <= y2:
            count += upper.count
            upper = upper.next

        lower.parent.next = upper
        if upper is not None:
            upper.parent = lower.parent

print(n - count)
