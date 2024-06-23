class SegmentTree:
    def __init__(self, array, op=sum):
        self.n = len(array)
        self.op = op
        self.T = [0]*self.n + array
        for i in range(self.n-1, 0, -1):
            self.T[i] = self.op((
                self.T[self.left(i)],
                self.T[self.right(i)]
            ))

    def __repr__(self):
        return str(self.T)

    @property
    def root(self):
        return self.T[1]

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1

    def parent(self, i):
        return i // 2

    def index(self, i):
        return self.n + i

    def sibling(self, i):
        return i+1 if i % 2 == 0 else i-1

    def update(self, i, val):
        i = self.index(i)
        self.T[i] = val
        while i > 1:
            parent = self.parent(i)
            self.T[parent] = self.op((
                self.T[i],
                self.T[self.sibling(i)]
            ))
            i = parent

    # [l, r], inclusive on both sides
    def _query(self, l, r):
        if l == r:
            yield self.T[self.index(l)]
            return

        l = self.index(l)
        r = self.index(r)
        yield self.T[l]
        yield self.T[r]

        while True:
            pl = self.parent(l)
            pr = self.parent(r)
            if pl == pr:
                return
            if l % 2 == 0:
                yield self.T[self.sibling(l)]
            if r % 2 == 1:
                yield self.T[self.sibling(r)]
            l, r = pl, pr

    def query(self, l, r):
        return self.op(self._query(l, r))
