import sys; input=sys.stdin.readline

INF = 2**60
n, f, T = map(int, input().split())
arr = [int(x) for x in input().split()]

N = (n*(n+1))//2
dp = [[-1]*(f+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(N-i, -1, -1):
        for k in range(f-1, -1, -1):
            if dp[j][k] == -1: continue
            dp[j+i][k+1] = max(dp[j+i][k+1], dp[j][k] + arr[i])
res = INF
for j in range(N+1):
    for k in range(f+1):
        if dp[j][k] >= T:
            res = min(res, j - (k*(k-1))//2)
print(res if res != INF else "NO")
