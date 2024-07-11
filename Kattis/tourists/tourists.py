from sys import stdin, stdout


def anc(x, k):
    if k == 0: 
        return x
    n = (k-1).bit_length()
    if k & (k-1) == 0:
        return anc_matrix[n][x]

    for j in range(n-1, -1, -1):
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

    return anc_matrix[0][v]


def lca_path_search(u, v):
    w = lca(u, v)
    return (depth[u] - depth[w]) + (depth[v] - depth[w]) + 1


n = int(stdin.readline())
log_n = n.bit_length()
depth = [0]*(n+1)
g = [[] for _ in range(n+1)]
anc_matrix = [[-1 for _ in range(n+1)] for _ in range(log_n)]
for _ in range(n-1):
    i, j = map(int, stdin.readline().split())
    g[i].append(j)
    g[j].append(i)

anc_matrix[0][1] = 0
stack = [1]
while stack:
    v = stack.pop()
    for u in g[v]:
        if anc_matrix[0][u] == -1:
            anc_matrix[0][u] = v
            stack.append(u)
            depth[u] = depth[v] + 1

for i in range(1, log_n):
    for j in range(1, n+1):
        anc_matrix[i][j] = anc_matrix[i-1][anc_matrix[i-1][j]]

s = sum(depth) + n-1
for i in range(2, n//2 + 1):
    for j in range(i*2, n+1, i):
        s += lca_path_search(i, j)
stdout.write(str(s))