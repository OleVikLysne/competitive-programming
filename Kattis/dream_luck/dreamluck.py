import sys; input=sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
if k == 1:
    print(1)
    exit()

occ = defaultdict(list)
for i, x in enumerate(map(int, input().split())):
    occ[x].append(i)

def check(arr, mi):
    l = 0
    maxl = 0
    for r in range(len(arr)):
        while arr[r] - arr[l] + 1 >= k:
            if l != maxl and mi > (l - maxl) /  (arr[l] - arr[maxl]):
                maxl = l
            l += 1
        if (r-l+1)/k > mi or (r-maxl+1) / max(k, (arr[r] - arr[maxl]+1)) > mi:
            return True
    return False


def eval(arr):
    lo, hi = 0, 1
    while hi - lo > 1e-6:
        mi = (lo+hi)/2
        if check(arr, mi):
            lo = mi
        else:
            hi = mi
    return lo

print(max(eval(arr) for arr in occ.values()))
