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

MAX = 100_001
n = int(input())
tree = FenwickTree(MAX)
prev = [0]*MAX
for i in range(n):
    l, r = map(int, input().split())
    lq = tree.query(l)
    rq = tree.query(r)
    sys.stdout.write(f"{lq + rq - prev[l] - prev[r]} ")
    prev[l] = lq
    prev[r] = rq
    tree.update(l+1, 1)
    tree.update(r, -1)