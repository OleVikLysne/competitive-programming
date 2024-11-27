import sys; input=sys.stdin.readline


def solve(i, adj_n, selected):
    if selected == (1 << len(adj_n))-1:
        return True
    if selected & 1 << i:
        return solve(i+1, adj_n, selected)
    for u, v in adj_n[i]:
        if not (selected & 1 << u or selected & 1 << v):
            if solve(i+1, adj_n, selected | 1 << u | 1 << v | 1 << i):
                return True
    return False


while (n := int(input())) != 0:
    name_to_idx = {}
    masks = []
    g = []
    for _ in range(n):
        p1, p2 = input().split()
        p1 = name_to_idx.setdefault(p1, len(name_to_idx))
        p2 = name_to_idx.setdefault(p2, len(name_to_idx))
        if p1 >= len(masks):
            masks.append(0)
            g.append([])
        if p2 >= len(masks):
            masks.append(0)
            g.append([])
        masks[p1] |= 1 << p2
        masks[p2] |= 1 << p1
        g[p1].append(p2)
        g[p2].append(p1)
    if len(masks) % 3 != 0:
        print("impossible")
        continue
    adj_n = [[] for _ in range(len(g))]
    for i in range(len(g)):
        for j in range(len(g[i])):
            for k in range(j+1, len(g[i])):
                u, v = g[i][j], g[i][k]
                if masks[u] & 1 << v:
                    adj_n[i].append((u, v))

    print("possible" if solve(0, adj_n, 0) else "impossible")
