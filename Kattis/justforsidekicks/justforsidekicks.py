from sys import stdin, stdout
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
            #self.T = [val]*self.n + array + [val]*pad_amount
            self.T = [val]*self.n
            self.T.extend(array)
            self.T.extend(val for _ in range(pad_amount))
        else:
            self.n = len(array)
            self.T = [val]*self.n
            self.T.extend(array)
            #self.T = [val]*self.n + array

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



n, q = map(int, stdin.readline().split())
V = [int(x) for x in stdin.readline().split()]
gems = [int(x)-1 for x in stdin.readline().rstrip()]
trees = [SegmentTree([int(i == k) for i in gems]) for k in range(6)]

for _ in range(q):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        k = b-1
        p = c-1
        old_p = gems[k]
        trees[old_p].update(k, 0)
        trees[p].update(k, 1)
        gems[k] = p

    elif a == 2:
        p = b-1
        v = c
        V[p] = v

    elif a == 3:
        l, r = b-1, c-1
        s = sum(tree.query(l, r) * V[i] for i, tree in enumerate(trees))
        stdout.write(str(s)+"\n")
