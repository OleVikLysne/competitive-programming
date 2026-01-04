import sys; input=sys.stdin.readline

n, k = map(int, input().split())
arr = [int(x) for x in input().split()]

INF = 2**60
dp = [[-INF]*(k+1) for _ in range(n)]
for i in range(n):
    dp[i][0] = 0
dp[0][1] = arr[0]

dp_inc = [[-INF]*(k+1) for _ in range(n)]
dp_inc[0][1] = arr[0]

for i in range(1, n):
    for j in range(1, k+1):
        dp_inc[i][j] = max(dp_inc[i-1][j], dp[i-1][j-1]) + arr[i]
        dp[i][j] = max(dp[i-1][j], dp_inc[i][j])

print(dp[n-1][k])