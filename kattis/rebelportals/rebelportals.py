import sys; input=sys.stdin.readline
import math

INF = 2**60
B = 7_000_000

n = int(input())
points = [tuple(map(float, input().split())) for _ in range(n)]
dist = [0]*(n**2)
for i in range(n):
    for j in range(i+1, n):
        dist[i*n+j] = dist[j*n+i] = int(math.dist(points[i], points[j])*B)

M = 1 << (n+1)
dp = [INF]*(M*n)

for i in range(1, n):
    dp[i*M+(1<<i)] = dist[i]

for mask in range(1 << n):
    for i in range(n):
        if mask & 1 << i == 0: continue
        x = z = dp[i*M+mask | (1 << n)]
        y = dp[i*M+mask]
        if x > y:
            dp[i*M+mask | (1 << n)] = y
            z = y
        for j in range(n):
            if mask & 1 << j: continue
            k = j*M+(mask | 1 << j)
            dp[k] = min(dp[k], z + dist[i*n+j])
            k |= 1 << n
            dp[k] = min(dp[k], y)

print(dp[(1 << (n+1))-1]/B)