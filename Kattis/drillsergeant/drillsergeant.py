import sys; input=sys.stdin.readline

class FenwickTree:
    def __init__(self, param):
        if isinstance(param, int):
            self.n = param
            self.tree = [0] * (self.n + 1)
        else:  # list
            self.n = len(param)
            self.tree = self.construct(param)

    def construct(self, arr):
        tree = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            tree[i] += arr[i-1]
            if (j := i + (i & -i)) <= self.n:
                tree[j] += tree[i]
        return tree

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

    # [l, r]
    def sum(self, l, r):
        return self.query(r) - self.query(l - 1)


n, m = map(int, input().split())
s = set()
edges = [tuple(map(int, input().split())) for _ in range(m)]
for u, v in edges:
    s.add(u)
    s.add(v)

q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]
for _, z in queries:
    s.add(z)

m = {x : i for i, x in enumerate(sorted(s))}
n = len(m)

H = [set() for _ in range(n)]
for u, v in edges:
    u = m[u]
    v = m[v]
    H[u].add(v)
    H[v].add(u)


def behind(v):
    if v == -1:
        return -1
    lo, hi = v, n
    while lo < hi:
        mi = (lo+hi)//2
        if tree.sum(v, mi) == 1:
            lo = mi + 1
        else:
            hi = mi
    return lo

def front(v):
    if v == n:
        return n
    lo, hi = 0, v
    while lo < hi:
        mi = (lo+hi)//2
        if tree.sum(mi, v) == 1:
            hi = mi
        else:
            lo = mi + 1
    return lo - 1

def calc(v, b, f):
    if v == -1 or v == n:
        return 0
    x, y = f in H[v], b in H[v]
    if x and y:
        return 3233
    elif x and not y:
        return 323
    elif not x and y:
        return 32
    return 3

tree = FenwickTree(n)
A = [(n, n)]*(n+2)
tot = 0
res = [0]*q
for i in range(q):
    d, v = queries[i]
    v = m[v]
    if d == 1:
        tree.update(v, 1)
        b = behind(v)
        f = front(v)
        for u in (b, f):
            tot -= calc(u, A[u][0], A[u][1])
        A[v] = (b, f)
        A[b] = (A[b][0], v)
        A[f] = (v, A[f][1])
        for u in (v, b, f):
            tot += calc(u, A[u][0], A[u][1])
    else:
        tree.update(v, -1)
        b, f = A[v]
        for u in (v, b, f):
            tot -= calc(u, A[u][0], A[u][1])
        A[v] = (n, n)
        A[b] = (A[b][0], front(b))
        A[f] = (behind(f), A[f][1])
        for u in (b, f):
            tot += calc(u, A[u][0], A[u][1])

    res[i] = tot

print("\n".join(map(str, res)))
