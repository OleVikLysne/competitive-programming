import sys; input=sys.stdin.readline

n, m = map(int, input().split())
N = [0]*n
for _ in range(m):
    u, v = map(int, input().split())
    N[v] |= 1 << u
    N[u] |= 1 << v

def bronkerbosch(r, p, x):
    if not p and not x:
        return r.bit_count()
    pux = p | x
    pivot = 0
    while pux & 1 == 0:
        pux >>= 1
        pivot += 1

    res = 0
    for v in range(n):
        if p & 1 << v and not N[pivot] & 1 << v:
            res = max(res, bronkerbosch(r | (1 << v), p & N[v], x & N[v]))
            p ^= 1 << v
            x |= 1 << v
    return res
print(bronkerbosch(0, (1 << n) - 1, 0))
