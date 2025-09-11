from collections import deque
import bisect

n, k = map(int, input().split())
arr = [int(x)-1 for x in input().split()]
pfs = [[0]*(n+1) for _ in range(32)]

for i in range(n):
    pfs[arr[i]][i+1] += 1
    for j in range(32):
        pfs[j][i+1] += pfs[j][i]

def sum(i, l, r):
    return pfs[i][r+1] - pfs[i][l]

dp = [0]*(n+1)
idxs = list(range(32))
next = [deque([n]*k) for _ in range(32)]

for l in range(n-1, -1, -1):
    dp[l] = dp[l+1]
    x = arr[l]
    next[x].popleft()
    next[x].append(l)
    idxs.remove(x)
    bisect.insort(idxs, x, key = lambda x: next[x][0])
    for i in range(32):
        r = next[idxs[i]][0]
        if r == n:
            break
        next_res = 2**(i+1) + dp[r+1]
        if next_res <= dp[l]:
            continue
        in_range = 0
        for j in range(i+1):
            in_range += sum(idxs[j], l, r)
        if in_range == r - l + 1:
            dp[l] = next_res
print(dp[0])