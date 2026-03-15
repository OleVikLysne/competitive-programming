import sys; input=sys.stdin.readline

B = 10**18+7
A = 31

class SegmentTree:
    def __init__(self, array, op=sum, pad = False):
        self.op = op
        if op == max:
            val = -2**62
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
            self.T[i] = self.op((
                self.T[self.left(i)],
                self.T[self.right(i)]
            ))

    def __repr__(self):
        return str(self.T)

    @property
    def root(self):
        return self.T[1]
    
    def index(self, i):
        return self.n + i

    def reverse_index(self, i):
        return i - self.n
    
    def is_leaf(self, i):
        return i >= self.n
    
    def parent(self, i):
        return i >> 1

    def sibling(self, i):
        return i+1 if i % 2 == 0 else i-1
    
    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def update(self, i, val):
        i = self.index(i)
        self.T[i] = val
        while (i := self.parent(i)) > 0:
            self.T[i] = self.op((
                self.T[self.left(i)],
                self.T[self.right(i)]
            ))

    # [l, r], inclusive on both sides
    def _query(self, l, r):
        if l == r:
            yield self.T[self.index(l)]
            return

        l = self.index(l)
        r = self.index(r)
        yield self.T[l]
        yield self.T[r]
        while (pl := self.parent(l)) != (pr := self.parent(r)):
            if l % 2 == 0:
                yield self.T[l+1]
            if r % 2 == 1:
                yield self.T[r-1]
            l, r = pl, pr

    def query(self, l, r):
        return (self.op(self._query(l, r)) * pow(A, l, B)) % B

def op(*args):
    return sum(*args) % B

s = input().rstrip()
k = len(s)-1
arr = [(ord(char) * pow(A, k-i, B)) % B for i, char in enumerate(s)]
tree = SegmentTree(arr, op=op)
for _ in range(int(input())):
    l, r = map(int, input().split())
    print(tree.query(l, r-1))