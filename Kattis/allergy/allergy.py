n = int(input())
D = [int(input()) for _ in range(n)]

dp = [[2**60]*(1 << n) for _ in range(8)]

for i in range(n):
    dp[D[i]][1 << i] = 0
for mask in range(1, 1 << n):
    for i in range(n):
        if mask & 1 << i:
            continue
        for d in range(1, 8):
            j = max(d, D[i]) - d + 1
            dp[j][mask | 1 << i] = min(
                dp[j][mask | 1 << i],
                d + dp[d][mask]
            )
print(min(dp[d][(1 << n) - 1] + d for d in range(8)))
