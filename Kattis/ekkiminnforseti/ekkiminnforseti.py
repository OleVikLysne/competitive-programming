import sys; input=sys.stdin.readline

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

    def update(self, i):
        i += self.n
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


n, m = map(int, input().split())
names = [input() for _ in range(m)]
matrix = [[int(x)-1 for x in reversed(input().split())] for _ in range(n)]
counts = [0]*m
mapping = [[] for _ in range(m)]
for i in range(n):
    cand = matrix[i].pop()
    counts[cand] += 1
    mapping[cand].append(i)
    
def cmp(x, y):
    if counts[x] <= counts[y]:
        if counts[x] == counts[y]:
            return max(x, y)
        return x
    return y

tree = SegmentTree([x for x in range(m)], op=cmp)
eliminated = [False]*m
for _ in range(m-1):
    i = tree.tree[1]
    eliminated[i] = True
    for j in mapping[i]:
        while eliminated[k := matrix[j].pop()]:...
        mapping[k].append(j)
        counts[k] += 1
        tree.update(k)
    counts[i] = 2**60
    tree.update(i)
print(names[tree.tree[1]])