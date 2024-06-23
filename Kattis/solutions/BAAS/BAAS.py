from sys import stdin

n = int(stdin.readline())
mask = [int(x) for x in stdin.readline().split()]
g = [[] for _ in range(n)]
for i in range(n):
    for x in map(int, stdin.readline().split()[1:]):
        g[i].append(x-1)


dp = [0]*n
visited = [-1]*n
def dfs(v, skip):
    if visited[v] == skip: return
    visited[v] = skip
    s = 0
    for u in g[v]:
        dfs(u, skip)
        s = max(s, dp[u])
    
    if v != skip:
        s += mask[v]
    dp[v] = s
    
s = 2**60
for i in range(n):
    dfs(n-1, i)
    s = min(s, dp[n-1])
print(s)
