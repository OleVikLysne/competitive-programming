n, m = map(int, input().split())

grid = [[c == "W" for c in input()] for _ in range(n)]
target = [[c == "W" for c in input()] for _ in range(n)]

c = n+m
dp = [-1]*(1 << c)
dp[0] = sum(grid[i][j] == target[i][j] for j in range(m) for i in range(n))
for mask in range(1 << c):
    for k in range(c):
        if mask & 1 << k: continue
        w = b = l = 0
        if k < n:
            for j in range(m):
                if mask & 1 << (j+n): continue
                w += target[k][j]
                b += not target[k][j]
                l += grid[k][j] == target[k][j]
        else:
            for i in range(n):
                if mask & 1 << i: continue
                w += target[i][k-n]
                b += not target[i][k-n]
                l += grid[i][k-n] == target[i][k-n]

        dp[mask | (1 << k)] = max(
            dp[mask | (1 << k)],
            dp[mask] + max(w, b) - l
        )
print(max(dp))