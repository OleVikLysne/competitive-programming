import sys; input=sys.stdin.readline

class FenwickTree:
    def __init__(self, param):
        if isinstance(param, int):
            self.n = param
            self.tree = [0] * (self.n + 1)
        else:  # list
            self.n = len(param)
            self.tree = self.construct(param)

    def construct(self, arr):
        tree = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            tree[i] += arr[i-1]
            if (j := i + (i & -i)) <= self.n:
                tree[j] += tree[i]
        return tree

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    # [0, r]
    def query(self, r):
        r += 1
        res = 0
        while r > 0:
            res += self.tree[r]
            r -= r & -r
        return res

    # [l, r]
    def sum(self, l, r):
        return self.query(r) - self.query(l - 1)

def inversions(a, idx_map):
    tree = FenwickTree(n)
    res = 0
    for j in range(n-1, -1, -1):
        i = idx_map[a[j]]
        res += tree.query(i)
        tree.update(i, 1)
    return res


res = []
while (n := int(input())) != 0:
    a = [int(x)-1 for x in input().split()]
    b = [int(x)-1 for x in input().split()]
    bm = [-1]*n
    cm = [-1]*n
    for i, x in enumerate(map(int, input().split())):
        cm[x-1] = i
        bm[b[i]] = i
    x = inversions(a, bm) + inversions(a, cm) + inversions(b, cm)
    res.append(n*(n-1)//2 - x//2)

print("\n".join(map(str, res)))
