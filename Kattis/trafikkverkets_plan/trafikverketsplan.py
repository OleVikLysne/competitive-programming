import sys; input=sys.stdin.readline

def anc(x, k):
    if k == 0:
        return x
    log_k = (k-1).bit_length()
    if k & (k-1) == 0:
        return anc_matrix[log_k][x]

    for j in range(log_k-1, -1, -1):
        if k >> j & 1:
            x = anc_matrix[j][x]
    return x

def lca(u, v):
    if depth[v] > depth[u]:
        u, v = v, u
    u = anc(u, depth[u]-depth[v])
    if u == v:
        return v

    log_n = (depth[v]-1).bit_length()
    for i in range(log_n-1, -1, -1):
        if anc_matrix[i][u] != anc_matrix[i][v]:
            u = anc_matrix[i][u]
            v = anc_matrix[i][v]
    
    ancestor = anc_matrix[0][v]
    return max(1, ancestor)

def is_path(start, target):
    ancestor = lca(start, target)
    if depth[start]-depth[ancestor] > dir_jumps[start][0]:
        return False
    if depth[target]-depth[ancestor] > dir_jumps[target][1]:
        return False
    return True

n = int(input())
log_n = (n-1).bit_length()
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append((b, 1))
    g[b].append((a, 0))

depth = [-1]*(n+1)
anc_matrix = [[0 for _ in range(n+1)] for _ in range(log_n + 1)]
dir_jumps = [[0, 0] for _ in range(n+1)]
depth[1] = 0
stack = [1]
while stack:
    v = stack.pop()
    for u, t in g[v]:
        if depth[u] == -1:
            depth[u] = depth[v] + 1
            anc_matrix[0][u] = v
            dir_jumps[u][t] = dir_jumps[v][t] + 1
            stack.append(u)

for i in range(1, log_n):
    for j in range(1, n+1):
        anc_matrix[i][j] = anc_matrix[i-1][anc_matrix[i-1][j]]

q = int(input())
for _ in range(q):
    if is_path(*map(int, input().split())):
        sys.stdout.write("ja ")
    else:
        sys.stdout.write("nej ")