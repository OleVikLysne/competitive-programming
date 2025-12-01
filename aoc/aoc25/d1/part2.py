import sys

p = 50
N = 100
s = 0
for line in sys.stdin:
    dir = -1 if line[0] == "L" else 1
    x = int(line[1:])
    s += x // N
    x %= N
    for _ in range(x):
        p += dir
        p %= N
        if p == 0:
            s += 1
print(s)


