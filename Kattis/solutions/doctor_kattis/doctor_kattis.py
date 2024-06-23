from sys import stdin, stdout

DEFAULT_VAL = (-2**30,)


class SegmentTree:
    def __init__(self, array, op=sum):
        self.n = len(array)
        self.op = op
        self.tree = [DEFAULT_VAL]*self.n + array
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.op((self.tree[self.left(i)], self.tree[self.right(i)]))

    def __repr__(self):
        return str(self.tree)
    
    @property
    def root(self):
        return self.tree[1]

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1
    
    def parent(self, i):
        return i // 2
    
    def index(self, i):
        return self.n + i

    def update(self, i, val):
        i = self.index(i)
        self.tree[i] = val
        while i > 1:
            i = self.parent(i)
            self.tree[i] = self.op((
                self.tree[self.left(i)], 
                self.tree[self.right(i)]
                ))

    # [l, r], inclusive on both sides
    def _query(self, l, r):
        l = self.index(l)
        r = self.index(r)
        if l == r:
            yield self.tree[l]
            return
        
        yield self.tree[l]
        yield self.tree[r]
        while True:
            pl = self.parent(l)
            pr = self.parent(r)
            if pl == pr:
                return
            if l % 2 == 0:
                yield self.tree[l+1]
            if r % 2 == 1:
                yield self.tree[r-1]

            l, r = pl, pr


    def query(self, l, r):
        return self.op(self._query(l, r))
    

tree = SegmentTree([DEFAULT_VAL]*200_000, op=max)
n = int(stdin.readline())
i = 199_999
c = 0
cat_to_idx = {}
cats = []
for _ in range(n):
    q = int(stdin.read(2))
    if q == 0:
        name, level = stdin.readline().split()
        level = int(level)
        tree.update(i, (level, i))
        cat_to_idx[name] = i
        i -= 1
        c += 1
        cats.append(name)

    elif q == 1:
        name, level = stdin.readline().split()
        level = int(level)
        j = cat_to_idx[name]
        level += tree.tree[tree.index(j)][0]
        tree.update(j, (level, j))
    
    elif q == 2:
        name = stdin.readline().strip()
        j = cat_to_idx[name]
        tree.update(j, DEFAULT_VAL)
        c -= 1

    elif q == 3:
        if c == 0:
            stdout.write("The clinic is empty\n")
        else:
            stdout.write(str(cats[199_999-tree.root[1]])+"\n")
