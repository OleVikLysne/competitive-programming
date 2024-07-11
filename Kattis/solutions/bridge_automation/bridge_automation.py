n = int(input())
boats = [int(input()) for _ in range(n)]
dp = [0]*(n+1)
for i in range(1, n+1):
    best = float("inf")
    for k in range(1, i+1):
        s = dp[i-k] + max(boats[i-1] - boats[i-k] - 1800 + 20, 20*k) + 120
        best = min(best, s)
    dp[i] = best
print(dp[n])