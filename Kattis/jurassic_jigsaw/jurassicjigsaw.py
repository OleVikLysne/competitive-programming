import sys

input = sys.stdin.readline

n, k = map(int, input().split())


def eval_match(s1, s2):
    x = k
    for i in range(k):
        if s1[i] == s2[i]:
            x -= 1
    return x


strings = []
g = [[] for _ in range(n)]
edges = []
for j in range(n):
    s = tuple(ord(x) for x in input().rstrip())
    for i in range(len(strings)):
        x = eval_match(s, strings[i])
        g[i].append((j, x))
        g[j].append((i, x))
        edges.append((i, j, x))
    strings.append(s)


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        rank[y] += 1


def kruskal(edges, num_nodes):
    edges.sort(key=lambda x: x[2], reverse=True)
    selected_edges = []
    parent = [x for x in range(num_nodes)]
    rank = [0] * num_nodes
    tree_sum = 0

    while len(selected_edges) < num_nodes - 1:
        u, v, w = edges.pop()
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            selected_edges.append((u, v, w))
            tree_sum += w
            union(parent, rank, x, y)

    return selected_edges, tree_sum


selected_edges, unlikeness = kruskal(edges, n)
print(unlikeness)
for i, j, _ in selected_edges:
    print(i, j)
