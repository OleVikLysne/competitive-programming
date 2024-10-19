class SegmentTree:
    def __init__(self, array, op=sum, pad=False):
        if op == sum:
            val = 0
            self.op = lambda x, y: x + y
        elif op == max:
            val = -2**62
            self.op = op
        else: # op == min
            val = 2**62
            self.op = op

        if pad:
            self.n = 2**((len(array)-1).bit_length())
            pad_amount = self.n - len(array)
            self.tree: list = [val]*self.n
            self.tree.extend(array)
            self.tree.extend(val for _ in range(pad_amount))
        else:
            self.n = len(array)
            self.tree: list = [val]*self.n
            self.tree.extend(array)

        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.op(
                self.tree[2*i],
                self.tree[2*i+1]
            )

    def __repr__(self):
        return str(self.tree)

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.op(
                self.tree[2*i],
                self.tree[2*i+1]
            )

    # [l, r], inclusive on both sides
    def query(self, l, r):
        l += self.n
        r += self.n
        if l == r:
            return self.tree[l]

        res = self.op(self.tree[l], self.tree[r])
        pl = l >> 1
        pr = r >> 1
        while pl != pr:
            if l & 1 == 0:
                res = self.op(res, self.tree[l+1])
            if r & 1 == 1:
                res = self.op(res, self.tree[r-1])
            l, r = pl, pr
            pl >>= 1
            pr >>= 1
        return res