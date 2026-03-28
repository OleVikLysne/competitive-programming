

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




# General fenwick tree which also supports max/min (within limitations)
class FenwickTree:
    def __init__(self, param, op=lambda x, y: x + y, default=0):
        self.op = op
        self.default = default

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
