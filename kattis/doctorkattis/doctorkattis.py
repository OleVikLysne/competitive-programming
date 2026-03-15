from sys import stdin, stdout

DEFAULT_VAL = (-2**30,)

class SegmentTree:
    def __init__(self, array, op=sum):
        self.n = len(array)
        self.op = op
        val = DEFAULT_VAL

        self.T = [val]*self.n + array
        for i in range(len(self.T)-1, 0, -2):
            self.T[self.parent(i)] = self.op((
                self.T[i],
                self.T[self.sibling(i)]
            ))

    def __repr__(self):
        return str(self.T)

    @property
    def root(self):
        return self.T[1]
    
    def index(self, i):
        return self.n + i
    
    def parent(self, i):
        return i // 2

    def sibling(self, i):
        return i+1 if i % 2 == 0 else i-1

    def update(self, i, val):
        i = self.index(i)
        self.T[i] = val
        while (p := self.parent(i)) > 0:
            self.T[p] = self.op((
                self.T[i],
                self.T[self.sibling(i)]
            ))
            i = p

    # [l, r], inclusive on both sides
    def _query(self, l, r):
        if l == r:
            yield self.T[self.index(l)]
            return

        l = self.index(l)
        r = self.index(r)
        yield self.T[l]
        yield self.T[r]
        while (pl := self.parent(l)) != (pr := self.parent(r)):
            if l % 2 == 0:
                yield self.T[self.sibling(l)]
            if r % 2 == 1:
                yield self.T[self.sibling(r)]
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
        level += tree.T[tree.index(j)][0]
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
