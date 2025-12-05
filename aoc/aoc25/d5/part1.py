import sys

ranges = []
for line in sys.stdin:
    if not (line := line.rstrip()):
        break
    ranges.append((tuple(map(int, line.split("-")))))

s = 0
for line in sys.stdin:
    n = int(line)
    for l, r in ranges:
        if l <= n <= r:
            s += 1
            break
print(s)