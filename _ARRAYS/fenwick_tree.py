class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
        self.n = n

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    # [0, r]
    def query(self, r):
        r += 1
        s = 0
        while r > 0:
            s += self.tree[r]
            r -= r & -r
        return s