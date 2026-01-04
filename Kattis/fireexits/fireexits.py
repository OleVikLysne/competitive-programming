import io, os
Ø = io.BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: next(Ø)

INF = 2**60

n, d = map(int, input().split())
c = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

dp = [[INF]*(2*d+1) for _ in range(n)]
def dfs(v, prev):
    g[v].remove(prev)
    for u in g[v]:
        dfs(u, v)

    if len(g[v]) == 0:
        for i in range(d+1):
            dp[v][i] = c[v]
        for i in range(d+1, 2*d+1):
            dp[v][i] = 0
        return

    cost = c[v]
    for u in g[v]:
        cost += dp[u][2*d]
    dp[v][0] = cost

    for i in range(1, d+1):
        cost = 0
        for u in g[v]:
            cost += dp[u][2*d-i]
        dp[v][2*d-i+1] = cost
        for u in g[v]:
            dp[v][i] = min(
                dp[v][i],
                cost - dp[u][2*d-i] + dp[u][i-1]
            )
    for i in range(1, 2*d+1):
        dp[v][i] = min(dp[v][i], dp[v][i-1])

g[0].append(-1)
dfs(0, -1)
print(dp[0][d])