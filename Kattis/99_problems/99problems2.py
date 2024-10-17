import sys; input = sys.stdin.readline

class SegmentTree:
    def __init__(self, array, op=sum, pad = False):
        self.op = op
        if op == max:
            val = -1
        elif op == min:
            val = 2**62
        else:
            val = 0
        if pad:
            self.n = 2**((len(array)-1).bit_length())
            pad_amount = self.n - len(array)
            self.T: list = [val]*self.n
            self.T.extend(array)
            self.T.extend(val for _ in range(pad_amount))
        else:
            self.n = len(array)
            self.T: list = [val]*self.n
            self.T.extend(array)

        for i in range(self.n-1, 0, -1):
            self.T[i] = self.op(
                self.T[2*i],
                self.T[2*i+1]
            )

    def update(self, i, val):
        self.T[i] = val
        while i > 1:
            i >>= 1
            self.T[i] = self.op(
                self.T[2*i],
                self.T[2*i+1]
            )

    def strictly_harder(self, val):
        i = 1
        while i < self.n:
            k = 2*i
            if self.T[k] > val:
                i = k
            else:
                i = 2*i+1
        return i

    def not_harder(self, val):
        i = 1
        while i < self.n:
            k = 2*i+1
            if self.T[k] <= val:
                i = k
            else:
                i *= 2
        return i


n, q = map(int, input().split())
values = [int(x) for x in input().split()]
values.sort()
tree1 = SegmentTree(values, op=max, pad=True)
tree2 = SegmentTree(values, op=min, pad=True)
for _ in range(q):
    t, d = map(int, input().split())
    if t == 1:
        i = tree1.strictly_harder(d)
    else:
        i = tree2.not_harder(d)
    sys.stdout.write(f"{tree1.T[i]} ")
    tree1.update(i, -1)
    tree2.update(i, 2**62)