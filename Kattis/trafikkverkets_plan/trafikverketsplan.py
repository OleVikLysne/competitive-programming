import sys; input=sys.stdin.readline

def anc(v, k):
    if k == 0:
        return v
    log_k = (k-1).bit_length()
    if k & (k-1) == 0:
        return anc_matrix[log_k][v]

    for i in range(log_k-1, -1, -1):
        if k >> i & 1:
            v = anc_matrix[i][v]
    return v


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


def build_anc_matrix(g: list[list[int]]):
    n = len(g)
    log_n = (n-1).bit_length()
    depth = [-1]*n
    depth[0] = 0
    anc_matrix = [[0]*n for _ in range(log_n)]

    stack = [0]
    while stack:
        v = stack.pop()
        for u, t in g[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                anc_matrix[0][u] = v
                stack.append(u)
                dir_jumps[u][t] = dir_jumps[v][t] + 1

    for i in range(1, log_n):
        for j in range(1, n):
            anc_matrix[i][j] = anc_matrix[i-1][anc_matrix[i-1][j]]

    return depth, anc_matrix
    


def is_path(start, target):
    ancestor = lca(start, target)
    if depth[start]-depth[ancestor] > dir_jumps[start][0]:
        return False
    if depth[target]-depth[ancestor] > dir_jumps[target][1]:
        return False
    return True

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = (int(x)-1 for x in input().split())
    g[a].append((b, 1))
    g[b].append((a, 0))


dir_jumps = [[0, 0] for _ in range(n)]
depth, anc_matrix = build_anc_matrix(g)

q = int(input())
for _ in range(q):
    if is_path(*(int(x)-1 for x in input().split())):
        sys.stdout.write("ja ")
    else:
        sys.stdout.write("nej ")