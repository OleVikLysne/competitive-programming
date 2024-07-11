anc_matrix: list[list[int]] = ...
depth: list[int] = ...

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

    return anc_matrix[0][v]