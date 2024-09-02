import sys; input=sys.stdin.readline


def search(x, k, anc_matrix, goal):
    if k == 0:
        return x == goal
    log_k = (k-1).bit_length()
    if k & (k-1) == 0:
        return goal in anc_matrix[log_k][x]

    for j in range(log_k-1, -1, -1):
        if k >> j & 1:
            for y in anc_matrix[j][x]:
                if search(y, k - 2**j, anc_matrix, goal):
                    return True
            return False
    return False


def reverse_graph(g):
    pos_roots = set(range(1, n+1))
    new_g = [[] for _ in range(len(g))]
    for v in range(len(g)):
        for u in g[v]:
            new_g[u].append(v)
            pos_roots.discard(v)
    return new_g, pos_roots

def build_depth_and_matrix(g, pos_roots):

    anc_matrix = [[[] for _ in range(n+1)] for _ in range(log_n + 1)]
    depth = [[] for _ in range(n+1)]
    stack = [(x, 0) for x in pos_roots]
    while stack:
        v, d = stack.pop()
        for u in g[v]:
            if v not in anc_matrix[0][u]:
                depth[u].append(d+1)
                anc_matrix[0][u].append(v)
            stack.append((u, d+1))

    for i in range(1, log_n):
        for j in range(1, n+1):
            for x in anc_matrix[i-1][j]:
                for y in anc_matrix[i-1][x]:
                    anc_matrix[i][j].append(y)



    # for i in range(1, log_n):
    #     for j in range(1, n+1):
    #         anc_matrix[i][j] = anc_matrix[i-1][anc_matrix[i-1][j]]
    return depth, anc_matrix


def is_path(start, target, anc_matrix, depth):
    for x in depth[start]:
        for y in depth[target]:
            if x > y:
                continue
            if search(target, y-x, anc_matrix, start):
                return True
    return False


n = int(input())
log_n = (n-1).bit_length()
g = [[] for _ in range(n+1)]
pos_roots = set(range(1, n+1))
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    pos_roots.discard(b)

depth_reg, anc_reg = build_depth_and_matrix(g, pos_roots)
depth_rev, anc_rev = build_depth_and_matrix(*reverse_graph(g))


for row in anc_reg:
    print(row)
print()
print(depth_reg)


q = int(input())
for _ in range(q):
    h, w = map(int, input().split())
    if is_path(h, w, anc_reg, depth_reg) and is_path(w, h, anc_rev, depth_rev):
        print("ja")
    else:
        print("nej")




