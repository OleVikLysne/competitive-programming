import sys; input=sys.stdin.readline

def mat_mul(A, B):
    return (
        (A[0] * B[0] + A[1] * B[2]) % MOD,
        (A[0] * B[1] + A[1] * B[3]) % MOD,
        (A[2] * B[0] + A[3] * B[2]) % MOD,
        (A[2] * B[1] + A[3] * B[3]) % MOD,
    )

def mat_pow(A, power):
    res = IDENTITY
    while power:
        if power & 1:
            res = mat_mul(res, A)
        A = mat_mul(A, A)
        power >>= 1
    return res

def mat_add(A, B):
    return (
        (A[0] + B[0]) % MOD,
        (A[1] + B[1]) % MOD,
        (A[2] + B[2]) % MOD,
        (A[3] + B[3]) % MOD,
    )

def fib(n):
    A = (1, 1, 1, 0)
    res = mat_pow(A, n)
    return res


IDENTITY = (1, 0, 0, 1)
EMPTY = (0, 0, 0, 0)
MOD = 10**9 + 7


class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.mat = IDENTITY
        self.tot = IDENTITY
        self.left = self.right = None

    def spread(self):
        if self.left is None:
            mid = (self.l + self.r)//2
            self.left = Node(self.l, mid)
            self.right = Node(mid, self.r)
        self.left.tot = mat_mul(self.left.tot, self.mat)
        self.left.mat = mat_mul(self.left.mat, self.mat)
        self.right.tot = mat_mul(self.right.tot, self.mat)
        self.right.mat = mat_mul(self.right.mat, self.mat)
        self.mat = IDENTITY


    def add(self, l, r, v):
        if self.l >= r or self.r <= l:
            return self.tot
        if l <= self.l and self.r <= r:
            self.tot = mat_mul(self.tot, v)
            self.mat = mat_mul(self.mat, v)
            return self.tot

        self.spread()
        self.tot = mat_add(
            self.left.add(l, r, v),
            self.right.add(l, r, v)
        )
        return self.tot

    
    def query(self, l, r):
        if self.l >= r or self.r <= l:
            return EMPTY
        if l <= self.l and self.r <= r:
            return self.tot
        self.spread()
        l_mat = self.left.query(l, r)
        r_mat = self.right.query(l, r)
        mat = mat_add(l_mat, r_mat)
        return mat


n, m = map(int, input().split())
tree = Node(0, n)
for i, x in enumerate(map(int, input().split())):
    tree.add(i, i+1, fib(x))

res = []
for _ in range(m):
    qt, l, r, *d = map(int, input().split())
    l -= 1
    r -= 1
    if qt == 1:
        d = d[0]
        v = fib(d)
        tree.add(l, r+1, v)
    else:
        res.append(tree.query(l, r+1)[1])
print(*res)
