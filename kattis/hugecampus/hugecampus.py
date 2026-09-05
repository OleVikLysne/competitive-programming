import sys; input=sys.stdin.readline

INF = 2**60
n, c = map(int, input().split())
c += 1
L = [0]
for _ in range(n):
    L.extend(map(int, input().split()))
    L.append(0)

S = []
for _ in range(n):
    S.extend(input().rstrip())

N = len(L)
dp = [INF]*c**2
dp[0] = 0
for i in range(N-1):
    ndp = dp if S[i] == "S" else [INF]*c**2
    u, v = L[i], L[i+1]
    ndp[v*c+v] = min(ndp[v*c+v], dp[u*c+u] + 1)
    for k in range(c):
        ndp[v*c+k] = min(ndp[v*c+k], dp[u*c+k] + 1, dp[k*c+u] + 1)
    dp = ndp

print(min(dp))