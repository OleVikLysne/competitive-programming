import sys; input=sys.stdin.readline

DEFAULT = 2**60
n, k = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
intervals.sort(key=lambda x: x[1])

length = 1 << ((n - 1).bit_length())
tree = [DEFAULT]*(2*length)
def update(i, val):
    i += length
    tree[i] = val
    while i > 1:
        i >>= 1
        tree[i] = min(tree[2 * i], tree[2 * i + 1])

def less_or_eq(val):
    i = 1
    while i < length:
        if tree[2*i+1] <= val:
            i = 2*i+1
        else:
            i = 2*i
    return i-length, tree[i]

in_use = 0
count = 0
for i in range(n):
    x, y = intervals[i]
    j, val = less_or_eq(x)
    if val <= x:
        update(j, DEFAULT)
        in_use -= 1
    if in_use < k:
        update(i, y)
        count += 1
        in_use += 1
print(count)
