import sys; input=sys.stdin.readline

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    # [0, r]
    def query(self, r):
        r += 1
        res = 0
        while r > 0:
            res += self.tree[r]
            r -= r & -r
        return res

n = int(input())
C = [int(x) for x in input().split()]
C.sort()

tree = FenwickTree(n)
m = int(input())
res = [0]*m
for q, b in enumerate(map(int, input().split())):
    lo, hi = 0, n
    while lo < hi:
        mi = (lo+hi)//2
        if C[mi] - tree.query(mi) < b:
            lo = mi + 1
        else:
            hi = mi

    res[q] = n - lo
    tree.update(lo, 1)

print("\n".join(map(str, res)))