n = int(input())
boats = [int(input()) for _ in range(n)]
dp = [2**60]*(n+1)
dp[0] = 0
for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = min(
            dp[i], 
            dp[i-k] + max(boats[i-1] - boats[i-k] - 1800 + 20, 20*k) + 120
        )
print(dp[n])