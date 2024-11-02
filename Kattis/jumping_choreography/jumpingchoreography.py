import sys

input = sys.stdin.readline
MAX = 1_000_001


class FenwickTree:
    def __init__(self, param, op=lambda x, y: x+y):
        self.default = 0
        self.op = op
        if op == max:
            self.default = -2**62
        elif op == min:
            self.default = 2**62

        if isinstance(param, int):
            self.n = param
            self.tree = [self.default] * (self.n + 1)
        else:  # list
            self.n = len(param)
            self.tree = [self.default] * (self.n + 1)
            for i in range(1, self.n + 1):
                self.tree[i] = self.op(self.tree[i], param[i - 1])
                if (j := i + (i & -i)) <= self.n:
                    self.tree[j] = self.op(self.tree[j], self.tree[i])

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] = self.op(self.tree[i], val)
            i += i & -i

    # [0, r]
    def query(self, r):
        r += 1
        res = self.default
        while r > 0:
            res = self.op(res, self.tree[r])
            r -= r & -r
        return res

    # [l, r]
    def sum(self, l, r):
        return self.query(r) - self.query(l - 1)


def moves(n, k):
    sum_k = (k * (k + 1)) // 2
    while True:
        if sum_k >= n and (sum_k - n) % 2 == 0:
            return k
        k += 1
        sum_k += k


def update(pos, tree: FenwickTree, jump_arr, delta):
    # left
    tree.update(pos, -jump_arr[0][0] * delta)
    prev = jump_arr[0][0]
    for i in range(1, len(jump_arr)):
        step_size, k = jump_arr[i]
        p = pos - k + 1
        if p <= 0:
            break
        tree.update(p, delta * (prev - step_size))
        prev = step_size
    tree.update(0, delta * prev)

    # right
    prev = 0
    for step_size, k in jump_arr:
        p = pos + k
        if p >= MAX:
            break
        tree.update(p, delta * (step_size - prev))
        prev = step_size


def change_frog(pos, delta):
    if pos % 2 == 0:
        update(pos, even_tree, even, delta)
        update(pos, odd_tree, odd, delta)
    else:
        update(pos, even_tree, odd, delta)
        update(pos, odd_tree, even, delta)


def query(t):
    if t % 2 == 0:
        return even_tree.query(t)
    return odd_tree.query(t)


even = [(3, 2)]
odd = [(1, 1)]
for i in range(3, MAX, 2):
    m = moves(i, odd[-1][0])
    if m != odd[-1][0]:
        odd.append((m, i))

for i in range(4, MAX, 2):
    m = moves(i, even[-1][0])
    if m != even[-1][0]:
        even.append((m, i))

even_tree = FenwickTree(MAX)
odd_tree = FenwickTree(MAX)

n, t = map(int, input().split())
for i in map(int, input().split()):
    change_frog(i, 1)
c = int(input())
for _ in range(c):
    qt, i = input().split()
    i = int(i)
    if qt == "t":
        t = i
    elif qt == "+":
        change_frog(i, 1)
    else:
        change_frog(i, -1)

    sys.stdout.write(f"{query(t)} ")
