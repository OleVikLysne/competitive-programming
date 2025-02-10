class SegmentTree:
    def __init__(self, array, op=lambda x, y: x + y, default=0):
        self.op = op
        self.default = default
        self.n = len(array)
        self.tree = [self.default] * self.n
        self.tree.extend(array)

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def __repr__(self):
        return str(self.tree)

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    # [l, r], inclusive on both sides
    def query(self, l, r):
        if l > r:
            return self.default
        if l == r:
            return self.tree[l + self.n]
        l += self.n
        r += self.n
        res = self.op(self.tree[l], self.tree[r])
        while l + 1 < r:
            if l & 1 == 0:
                res = self.op(res, self.tree[l + 1])
            if r & 1 == 1:
                res = self.op(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
