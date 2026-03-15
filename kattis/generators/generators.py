import sys; input = sys.stdin.readline

n, m = map(int, input().split())

G = [2**60]*n
for _ in range(m):
    c, x = map(int, input().split())
    G[c-1] = x

E = [int(x) for x in input().split()]
k = (E.index(max(E)) + 1) % n
E = E[k:] + E[:k]
G = G[k:] + G[:k]

dp = [[-1]*n for _ in range(2)]
dp[0][n-1] = G[n-1]
dp[1][n-1] = 0
for i in range(n-2, -1, -1):
    dp[0][i] = min(
        G[i] + E[i] + dp[1][i+1], 
        min(G[i], E[i]) + dp[0][i+1]
    )
    dp[1][i] = min(
        E[i] + dp[1][i+1],
        dp[0][i+1]
    )
print(dp[0][0])
