from sys import stdin

n, m = map(int, stdin.readline().split())
forced = [[] for _ in range(n)]
buggy = [[] for _ in range(n)]
for _ in range(m):
    i, j = [int(x) for x in stdin.readline().split()]
    if i < 0:
        i = abs(i)
        forced[i-1].append(j-1)
    else:
        buggy[i-1].append(j-1)

visited = [False]*n
s = 0
def dfs(v, bug_move=False):
    global s
    visited[v] = True
    if not forced[v]:
        s += 1
    for u in forced[v]:
        if not visited[u]:
            dfs(u, bug_move=bug_move)
    if not bug_move:
        for u in buggy[v]:
            if not visited[u]:
                dfs(u, bug_move=True)

dfs(0)
print(s)