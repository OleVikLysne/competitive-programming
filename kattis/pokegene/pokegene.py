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
        for u in g[v]:
            if u == -1: continue
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                anc_matrix[0][u] = v
                stack.append(u)

    for i in range(1, log_n):
        for j in range(n):
            anc_matrix[i][j] = anc_matrix[i-1][anc_matrix[i-1][j]]

    return depth, anc_matrix    

##################################

g = []
prev = []
def new_node():
    g.append([])
    prev.append(-1)
    return len(g)-1

def add(string):
    current = root
    for char in string:
        x = ord(char)
        if x != prev[current]:
            y = new_node()
            g[current].append(y)
            prev[current] = x
        current = g[current][-1]
    return current

root = new_node()
n, q = map(int, input().split())
strings = [(i, input().rstrip()) for i in range(n)]
strings.sort(key=lambda x: x[1])
sort_map = [-1]*n
nodes = []
for i in range(n):
    j, string = strings[i]
    sort_map[j] = i
    nodes.append(add(string))

depth, anc_matrix = build_anc_matrix(g, root=root)

for _ in range(q):
    k, l = map(int, input().split())
    indices = [sort_map[int(x)-1] for x in input().split()]
    indices.sort()
    tot = 0
    for i in range(k-l+1):
        a = nodes[indices[i]]
        b = nodes[indices[i+l-1]]
        c = lca(a, b)
        d = lca(c, nodes[indices[i+l]]) if i+l <  k else root
        e = lca(c, nodes[indices[i-1]]) if i-1 >= 0 else root
        tot += depth[c] - max(depth[d], depth[e])
    print(tot)