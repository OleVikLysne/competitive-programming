import sys; input=sys.stdin.readline

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
            self.T = [val]*self.n + array + [val]*pad_amount
        else:
            self.n = len(array)
            self.T = [val]*self.n + array

        for i in range(self.n-1, 0, -1):
            self.T[i] = self.op(
                self.T[2*i],
                self.T[2*i+1]
            )

    def __repr__(self):
        return str(self.T)

    def update(self, i, val):
        i += self.n
        self.T[i] = val
        while i > 1:
            i >>= 1
            self.T[i] = self.op(
                self.T[2*i],
                self.T[2*i+1]
            )

    # [l, r], inclusive on both sides
    def query(self, l, r):
        l += self.n
        r += self.n
        if l == r:
            return self.T[l]

        res = self.op(self.T[l], self.T[r])
        pl = l >> 1
        pr = r >> 1
        while pl != pr:
            if l & 1 == 0:
                res = self.op(res, self.T[l+1])
            if r & 1 == 1:
                res = self.op(res, self.T[r-1])
            l, r = pl, pr
            pl >>= 1
            pr >>= 1
        return res


n, k = map(int, input().split())
arr1 = [int(x)-1 for x in input().split()]
arr2 = [int(x)-1 for x in input().split()]


m = [[] for _ in range(n)]
for i in range(n*k-1, -1, -1):
    m[arr2[i]].append(i)

tree = SegmentTree([0]*(n*k), op=max)
for x in arr1:
    for i in m[x]:
        v = tree.query(0, i-1) if i > 0 else 0
        tree.update(i, v+1)
print(tree.query(0, n*k-1))