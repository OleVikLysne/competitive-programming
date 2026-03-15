# time limit in python, same logic fast enough in rust

import sys; input=sys.stdin.readline
n, T = map(int, input().split())
prize = [-1]*n
time = [-1]*n
deadline = [-1]*n
INF = 2**30
for i in range(n):
    p, t, d = map(int, input().split())
    if d == -1:
        d = INF
    prize[i] = p
    time[i] = t 
    deadline[i] = d
dist = [[int(x) for x in input().split()] for _ in range(n+2)]

def check(t, i, j):
    temp = t + dist[i][j] + time[j]
    if temp > deadline[j] or temp + dist[j][n+1] > T:
        return False
    return True

bits = [[] for _ in range(n)]
for i in range(1, 2**n):
    bits[i.bit_count()-1].append(i)


dp = [[INF]*(2**n) for _ in range(n)]
for i in range(n):
    if check(0, n, i):
        dp[i][1<<i] = dist[n][i] + time[i]


total, best_mask = 0, 0
for i in range(1, n):
    for mask in bits[i-1]:
        for j in range(0, n):
            t = dp[j][mask]
            if t == INF:
                continue
            tot = 0
            for k in range(n):
                if mask & 1 << k:
                    tot += prize[k]
                    continue
                if not check(t, j, k):
                    continue
                new_mask = mask | 1 << k
                dp[k][new_mask] = min(dp[k][new_mask], t + dist[j][k] + time[k])
            if tot > total or tot == total and mask < best_mask:
                total = tot
                best_mask = mask

for i in range(n):
    if dp[i][(1<<n)-1] != INF:
        total = sum(prize)
        best_mask = (1<<n)-1
        break
print(total)
print(*(i+1 for i in range(n) if best_mask & 1 << i))
