import sys
from collections import deque

inp = []
for line in sys.stdin:
    a, *args, c = line.split()
    target = 0
    for i, char in enumerate(a.strip("[]")):
        if char == "#":
            target |= 1 << i
    row = [target]
    for x in args:
        mask = 0
        for i in map(int, x.strip("()").split(",")):
            mask |= 1 << i
        row.append(mask)
    inp.append(row)

def solve(row):
    target, masks = row[0], row[1:]
    q = deque([(0, 0)])
    visited = {0}
    while q:
        s, m = q.popleft()
        if m == target:
            return s
        for mask in masks:
            x = m ^ mask
            if x not in visited:
                visited.add(x)
                q.append((s+1, x))


print(sum(solve(row) for row in inp))
