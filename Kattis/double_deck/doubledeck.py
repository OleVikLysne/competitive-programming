import sys; input=sys.stdin.readline

class FenwickTree:
    def __init__(self, param, op=lambda x, y: x+y):
        self.default = 0
        self.op = op
        if op == max:
            self.default = 0
        elif op == min:
            self.default = 2**62

        if isinstance(param, int):
            self.n = param
            self.tree = [self.default] * (self.n + 1)
        else:  # list
            self.n = len(param)
            self.tree = [self.default] * (self.n + 1)
            for i in range(1, self.n + 1):
                self.tree[i] = self.op(self.tree[i], param[i - 1])
                if (j := i + (i & -i)) <= self.n:
                    self.tree[j] = self.op(self.tree[j], self.tree[i])

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] = self.op(self.tree[i], val)
            i += i & -i

    # [0, r]
    def query(self, r):
        r += 1
        res = self.default
        while r > 0:
            res = self.op(res, self.tree[r])
            r -= r & -r
        return res

    # [l, r]
    def sum(self, l, r):
        return self.query(r) - self.query(l - 1)


n, k = map(int, input().split())
m = [[] for _ in range(n)]
for i, x in enumerate(map(int, input().split())):
    m[x-1].append(i)

tree = FenwickTree(n*k, op=max)
for x in map(int, input().split()):
    for j in range(k-1, -1, -1):
        i = m[x-1][j]
        v = tree.query(i-1)
        tree.update(i, v+1)
print(tree.query(n*k-1))