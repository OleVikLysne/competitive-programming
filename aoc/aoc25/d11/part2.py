import sys

g = {}
for line in sys.stdin:
    v, *arr = line.split()
    v = v.rstrip(":")
    g[v] = arr

START = "svr"
END = "out"
mem = {}
def solve(v, dac, fft):
    d = dac or v == "dac"
    f = fft or v == "fft"
    if v == END:
        return 1 if d and f else 0
    if (res := mem.get((v, dac, fft))) != None:
        return res
    res = 0
    for u in g[v]:
        res += solve(u, d, f)
    mem[(v, dac, fft)] = res
    return res

print(solve(START, False, False))