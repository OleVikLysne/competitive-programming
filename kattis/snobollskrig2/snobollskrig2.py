import sys; input=sys.stdin.readline

class SortedSearchTree:
    '''
        "op=min" to query for largest value which is less than / less than or equal to some value
        "op=max" to query for smallest value which is greater than / greater than or equal to some value
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
        return self._query_greater(val, lambda x, y: x > y)

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

n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a.sort()
b.sort()
a_tree = SortedSearchTree(a, op=max)
b_tree = SortedSearchTree(b, op=max)

min_idxs = [0, 0]
trees = [a_tree, b_tree]
arrays = [a, b]
visited = [[False]*n, [False]*m]
not_def = 0
while min_idxs[0] < len(arrays[0]) or min_idxs[1] < len(arrays[1]):
    i = 0
    j = 1
    if min_idxs[i] == len(arrays[i]) or min_idxs[j] < len(arrays[j]) and arrays[j][min_idxs[j]] < arrays[i][min_idxs[i]]:
        i, j = j, i
    cur = min_idxs[i]
    visited[i][min_idxs[i]] = True
    not_def += 1
    while cur < len(arrays[i]):
        while min_idxs[i] < len(arrays[i]) and visited[i][min_idxs[i]]:
            min_idxs[i] += 1
        val, idx = trees[j].gt(arrays[i][cur])
        if val <= arrays[i][cur]:
            break
        trees[j].reset(idx)
        visited[j][idx] = True
        cur = idx
        i, j = j, i

print(n+m-not_def)
