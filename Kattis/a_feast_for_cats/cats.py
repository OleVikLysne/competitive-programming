import sys; input=sys.stdin.readline

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
    parent = [x for x in range(num_nodes)]
    rank = [0] * num_nodes
    tree_sum = 0
    n = 0
    while n < num_nodes - 1:
        u, v, w = edges.pop()
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            tree_sum += w
            n += 1
            union(parent, rank, x, y)

    return tree_sum


for _ in range(int(input())):
    m, c = map(int, input().split())
    edges = []
    for _ in range((c*(c-1)//2)):
        edges.append(tuple(map(int, input().split())))
    if kruskal(edges, c) + c <= m:
        print("yes")
    else:
        print("no")