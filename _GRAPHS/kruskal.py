edges: list[tuple[int, int, int]] = ...  # u, v, w


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += 1
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
