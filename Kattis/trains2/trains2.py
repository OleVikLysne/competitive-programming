import sys; input = sys.stdin.readline

MOD = 10**9 + 7
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
thresh = 25  # math.isqrt(n)
sq = [[[0, 1] for _ in range(k)] for k in range(thresh)]
dp = [1] * n

for i in range(n - 1, -1, -1):
    d, x = arr[i]
    if d != 0:
        if d < thresh:
            a = sq[d][i % d]
            steps = min(x, (n - i - 1) // d)
            dp[i] += a[-1] - a[max(0, len(a) - 1 - steps)]
        else:
            for j in range(i + d, min(n, i + (d * x) + 1), d):
                dp[i] += dp[j]
        dp[i] %= MOD
    for k in range(1, thresh):
        a = sq[k][i % k]
        a.append((a[-1] + dp[i]) % MOD)
print(dp[0])
