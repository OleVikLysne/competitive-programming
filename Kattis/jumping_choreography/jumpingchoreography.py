import sys; input = sys.stdin.readline
MAX = 10**6 + 1

class FenwickTree:
    def __init__(self, param):
        self.n = param
        self.tree = [0] * (self.n + 1)


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

odd = [(0, 0), (1, 1)]
even = [(0, 0), (3, 2)]
for i in range(2, MAX):
    arr = even if i % 2 == 0 else odd
    k = arr[-1][0]
    sum_k = (k * (k + 1)) // 2
    while sum_k < i or (sum_k - i) % 2 != 0:
        k += 1
        sum_k += k
    if k != arr[-1][0]:
        arr.append((k, i))

def _update(p, d, tree: FenwickTree, jumps):
    prev = 0
    prev_pos = 0
    for cost, jump in reversed(jumps):
        if jump <= p:
            tree.update(prev_pos, d * (cost - prev))
            prev = cost
            prev_pos = (p - jump) // 2 + 1

    prev = 0
    for cost, jump in jumps:
        i = p + jump
        if i >= MAX:
            break
        tree.update(i//2, d * (cost - prev))
        prev = cost

def update(i, d):
    if i % 2 == 0:
        _update(i, d, et, even)
        _update(i, d, ot, odd)
    else:
        _update(i, d, et, odd)
        _update(i, d, ot, even)

def query(t):
    if t % 2 == 0:
        return et.query(t // 2)
    return ot.query(t // 2)

ot = FenwickTree(MAX // 2 + 1)
et = FenwickTree(MAX // 2 + 1)

_, t = map(int, input().split())
for i in map(int, input().split()):
    update(i, 1)

for _ in range(int(input())):
    qt, i = input().split()
    i = int(i)
    if qt == "t":
        t = i
    elif qt == "+":
        update(i, 1)
    else:
        update(i, -1)
    sys.stdout.write(f"{query(t)} ")