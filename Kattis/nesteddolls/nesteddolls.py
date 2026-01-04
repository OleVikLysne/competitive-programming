import sys; input=sys.stdin.readline

class SortedSearchTree:
    '''
        "op=min" for less than / less than or equal queries
        "op=max" for greater than / greater than or equal queries
    '''
    def __init__(self, param: int | None, op = min, default = None):
        self.op = op
        if default is not None:
            self.default = default
        elif op == min:
            self.default = 1 << 62
        else: #op = max
            self.default = -(1 << 62)
        if isinstance(param, list):
            self.n = 2**((len(param)-1).bit_length())
            self.tree: list = [self.default]*self.n
            self.tree.extend(param)
            self.tree.extend(self.default for _ in range(self.n - len(param)))
            for i in range(self.n-1, 0, -1):
                self.tree[i] = op(
                    self.tree[2*i],
                    self.tree[2*i+1]
                )
        else:
            self.n = 2**((param-1).bit_length())
            self.tree = [self.default]*(self.n*2)
    
    def _query_less(self, val, comp):
        i = 1
        while i < self.n:
            if comp(self.tree[2*i+1], val):
                i = 2*i+1
            else:
                i = 2*i
        return self.tree[i], i-self.n
    
    def _query_greater(self, val, comp):
        i = 1
        while i < self.n:
            if comp(self.tree[2*i], val):
                i = 2*i
            else:
                i = 2*i+1
        return self.tree[i], i-self.n

    def le(self, val):
        return self._query_less(val, lambda x, y: x <= y)

    def lt(self, val):
        return self._query_less(val, lambda x, y: x < y)
    
    def gt(self, val):
        #return self._query_greater(val, lambda x, y: x > y)
        return self._query_greater(val, lambda x, y: x[0] > y[0] and x[1] > y[1])

    def ge(self, val):
        return self._query_greater(val, lambda x, y: x >= y)
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.op(self.tree[2*i], self.tree[2*i+1])

    def reset(self, i):
        self.update(i, self.default)

for _ in range(int(input())):
    n = int(input())
    inp = input().split()
    dolls = [(int(inp[2*i]), int(inp[2*i+1]), i) for i in range(n)]
    dolls.sort(key=lambda x: x[1])
    mapping = [-1]*n
    for i in range(n):
        mapping[dolls[i][2]] = i
    tree = SortedSearchTree(n, op = max, default = (-1 << 60,))
    dolls.sort(key=lambda x: x[0], reverse=True)
    c = 0
    for w, h, i in dolls:
        j = mapping[i]
        entry = (h, w)
        val, idx = tree.gt(entry)
        if val > entry:
            tree.reset(idx)
        else:
            c += 1
        tree.update(j, entry)
    sys.stdout.write(f"{c} ")