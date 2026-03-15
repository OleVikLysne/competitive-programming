import sys; input=sys.stdin.readline

def anc(v: int, k: int):
    i = k.bit_length()-1
    while k:
        if k & 1 << i:
            v = anc_matrix[i][v]
        k &= (1 << i) - 1
        i -= 1
    return v


def lca(u: int, v: int):
    if depth[v] > depth[u]:
        u, v = v, u
    u = anc(u, depth[u]-depth[v])
    if u == v:
        return v

    log_d = (depth[v]-1).bit_length()
    for i in range(log_d-1, -1, -1):
        if anc_matrix[i][u] != anc_matrix[i][v]:
            u = anc_matrix[i][u]
            v = anc_matrix[i][v]

    return anc_matrix[0][v]


def build_anc_matrix(g: list[list[int]], root=0):
    n = len(g)
    log_n = (n-1).bit_length()
    depth = [-1]*n
    depth[root] = 0
    anc_matrix = [[-1]*n for _ in range(log_n)]
    stack = [root]
    while stack:
        v = stack.pop()
        for u, t in g[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                anc_matrix[0][u] = v
                stack.append(u)
                dir_jumps[u][t] = dir_jumps[v][t] + 1

    for i in range(1, log_n):
        for j in range(n):
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
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append((b, 1))
    g[b].append((a, 0))


dir_jumps = [[0, 0] for _ in range(n)]
depth, anc_matrix = build_anc_matrix(g, root=n//2)

q = int(input())
for _ in range(q):
    if is_path(*map(lambda x: int(x)-1, input().split())):
        sys.stdout.write("ja ")
    else:
        sys.stdout.write("nej ")