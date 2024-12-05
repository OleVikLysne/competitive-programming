
"""
    lowest common ancestor implementation using binary lifting
"""

anc_matrix: list[list[int]] = ...
depth: list[int] = ...


def anc(v: int, k: int):
    if k == 0:
        return v
    log_k = (k-1).bit_length()
    if k & (k-1) == 0:
        return anc_matrix[log_k][v]

    for i in range(log_k-1, -1, -1):
        if k >> i & 1:
            v = anc_matrix[i][v]
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


def build_anc_matrix(g: list[list[int]]):
    n = len(g)
    log_n = (n-1).bit_length()
    depth = [-1]*n
    depth[0] = 0
    anc_matrix = [[0]*n for _ in range(log_n)]

    stack = [0]
    while stack:
        v = stack.pop()
        for u in g[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                anc_matrix[0][u] = v
                stack.append(u)

    for i in range(1, log_n):
        for j in range(1, n):
            anc_matrix[i][j] = anc_matrix[i-1][anc_matrix[i-1][j]]

    return depth, anc_matrix
