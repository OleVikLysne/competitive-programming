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


n, q = map(int, input().split())
tree = FenwickTree(n)
c = 0
pancakes = [0]*n
for _ in range(q):
    t = sys.stdin.read(1)
    inp = input()
    if t == "1":
        i = int(inp)-1
        if pancakes[i] == 0:
            pancakes[i] = 1
            tree.update(i, 1)
        else:
            pancakes[i] = 0
            tree.update(i, -1)
    elif t == "2":
        c = (c+1) % 2
    else:
        l, r = 1, n
        if t == "4":
            l, r = map(int, inp.split())
        s = tree.sum(l-1, r-1)
        if c == 1:
            s = r-l+1-s
        sys.stdout.write(f"{s} ")
