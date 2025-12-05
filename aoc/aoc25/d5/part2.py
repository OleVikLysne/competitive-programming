import sys

ranges = []
for line in sys.stdin:
    if not (line := line.rstrip()):
        break
    ranges.append((tuple(map(int, line.split("-")))))


points = []
for l, r in ranges:
    points.append((l, 0))
    points.append((r+1, 1))
points.sort()
prev = points.pop(0)[0]
open = 1
s = 0
for x, y in points:
    if open:
        s += x - prev
    if y == 1:
        open -= 1
    else:
        open += 1
    prev = x
print(s)