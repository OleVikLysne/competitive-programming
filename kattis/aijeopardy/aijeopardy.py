def comb(n, k, limit):
    if k > n:
        return 0
    res = 1
    for i in range(k):
        res *= n-i
        res //= i+1
        if res > limit:
            return limit+1
    return res

x = int(input())
res = (x, 1)
for k in range(170):
    lo, hi = 0, 10**21
    while lo < hi:
        mi = (lo+hi)//2
        if comb(mi, k, x) < x:
            lo = mi + 1
        else:
            hi = mi
    if comb(lo, k, x) == x:
        res = min(res, (lo, k))
print(*res)