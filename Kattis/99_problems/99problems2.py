import sys; input = sys.stdin.readline

DEFAULT = (-1, 2**62)

class SegmentTree:
    def __init__(self, array):
        self.n = 2**(len(array)-1).bit_length()
        pad_amount = self.n - len(array)
        self.T = [DEFAULT]*self.n + [(x, x) for x in array] + [DEFAULT]*pad_amount
        for i in range(self.n-1, -1, -1):
            max_i, min_i = self.T[self.left(i)]
            max_j, min_j = self.T[self.right(i)]
            self.T[i] = (max((max_i, max_j)), min((min_i, min_j)))

    def index(self, i):
        return self.n + i
    
    def is_leaf(self, i):
        return i >= self.n

    def parent(self, i):
        return i >> 1

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def update(self, i):
        self.T[i] = DEFAULT
        while (p := self.parent(i)) > 0:
            max_i, min_i = self.T[self.left(p)]
            max_j, min_j = self.T[self.right(p)]
            self.T[p] = (max((max_i, max_j)), min((min_i, min_j)))
            i = p

    def strictly_harder(self, val):
        i = 1
        while not self.is_leaf(i):
            k = self.left(i)
            if self.T[k][0] > val:
                i = k
            else:
                i = self.right(i)
        return i

    def not_harder(self, val):
        i = 1
        while not self.is_leaf(i):
            k = self.right(i)
            if self.T[k][1] <= val:
                i = k
            else:
                i = self.left(i)
        return i
            


n, q = map(int, input().split())
values = [int(x) for x in input().split()]
values.sort()
tree = SegmentTree(values)
for _ in range(q):
    t, d = map(int, input().split())
    if t == 1:
        i = tree.strictly_harder(d)
    else:
        i = tree.not_harder(d)
    sys.stdout.write(f"{tree.T[i][0]} ")
    tree.update(i)