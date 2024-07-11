from sys import stdin, stdout


ROOT = 1
FAKE_ROOT = -1
nodes = [None, {}]
anc_matrix = [[FAKE_ROOT, 0]]
depth = [None, 0]


def new_node():
    nodes.append({})
    depth.append(0)
    anc_matrix[0].append(FAKE_ROOT)
    return len(nodes) - 1


def add(word):
    current_id = ROOT
    for char in word:
        current_node = nodes[current_id]
        if char not in current_node:
            current_node[char] = new_node()

        next_id = current_node[char]
        depth[next_id] = depth[current_id] + 1
        anc_matrix[0][next_id] = current_id
        current_id = next_id
    return current_id


def anc(x, k):
    if k == 0:
        return x
    log_k = (k - 1).bit_length()
    if k & (k - 1) == 0:
        return anc_matrix[log_k][x]
    for j in range(log_k - 1, -1, -1):
        if k >> j & 1:
            x = anc_matrix[j][x]
    return x


def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    u = anc(u, depth[u] - depth[v])
    if u == v:
        return u

    for i in range(log_n, -1, -1):
        if anc_matrix[i][u] != anc_matrix[i][v]:
            u = anc_matrix[i][u]
            v = anc_matrix[i][v]

    return anc_matrix[0][u]


mons = []
n, q = map(int, stdin.readline().split())
max_len = 0
for i in range(n):
    pokemon = stdin.readline().rstrip()
    node = add(pokemon)
    mons.append((node, pokemon, i))
    max_len = max(max_len, len(pokemon))

mons.sort(key=lambda x: x[1])
index_map = [0] * n
for i in range(n):
    j = mons[i][2]
    index_map[j] = i


log_n = (max_len - 1).bit_length()
num_nodes = len(anc_matrix[0])
anc_matrix.extend([FAKE_ROOT for _ in range(num_nodes)] for _ in range(log_n))
for i in range(1, log_n):
    for j in range(1, num_nodes):
        anc_matrix[i][j] = anc_matrix[i - 1][anc_matrix[i - 1][j]]


for _ in range(q):
    k, l = map(int, stdin.readline().split())
    indices = [index_map[int(x) - 1] for x in stdin.readline().split()]
    indices.sort()

    s = 0
    for i in range(k - l + 1):
        poke1 = mons[indices[i]][0]
        poke2 = mons[indices[i + l - 1]][0]
        lcp = depth[lca(poke1, poke2)]
        option1, option2 = 0, 0
        if i > 0:
            poke3 = mons[indices[i - 1]][0]
            option1 = depth[lca(poke1, poke3)]
        if i + l < k:
            poke4 = mons[indices[i + l]][0]
            option2 = depth[lca(poke1, poke4)]

        diff = max(option1, option2)
        s += max(lcp - diff, 0)
    stdout.write(str(s) + "\n")