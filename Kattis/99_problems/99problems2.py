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
            self.n = 2**(len(array)-1).bit_length()
            pad_amount = self.n - len(array)
            self.T = [val]*self.n + array + [val]*pad_amount
        else:
            self.n = len(array)
            self.T = [val]*self.n + array
        for i in range(self.n-1, 0, -1):
            self.T[i] = self.op(
                self.T[self.left(i)],
                self.T[self.right(i)]
            )
    
    
    def is_leaf(self, i):
        return i >= self.n
    
    def index(self, i):
        return self.n + i
    
    def parent(self, i):
        return i >> 1
    
    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def update(self, i, val):
        self.T[i] = val
        while (i := self.parent(i)) > 0:
            self.T[i] = self.op(
                self.T[self.left(i)],
                self.T[self.right(i)]
            )

    def strictly_harder(self, val):
        i = 1
        while not self.is_leaf(i):
            k = self.left(i)
            if self.T[k] > val:
                i = k
            else:
                i = self.right(i)
        return i

    def not_harder(self, val):
        i = 1
        while not self.is_leaf(i):
            k = self.right(i)
            if self.T[k] <= val:
                i = k
            else:
                i = self.left(i)
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