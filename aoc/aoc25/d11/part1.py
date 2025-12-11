import sys

g = {}
for line in sys.stdin:
    v, *arr = line.split()
    v = v.rstrip(":")
    g[v] = arr

START = "you"
END = "out"
mem = {}
def solve(v):
    if v == END:
        return 1
    if (res := mem.get(v)) != None:
        return res
    res = 0
    for u in g[v]:
        res += solve(u)
    mem[v] = res
    return res


print(solve(START))