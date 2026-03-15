from sys import stdin


def search(start):
    stacks = ([], [])

    deg = [x for x in degree]

    for i in range(n):
        if deg[i] == 0:
            stacks[mask[i]].append(i)

    i = start
    c = -1
    while stacks[0] or stacks[1]:
        while stacks[i]:
            v = stacks[i].pop()
            for u in g[v]:
                deg[u] -= 1
                if deg[u] == 0:
                    stacks[mask[u]].append(u)
        c += 1
        i = (i + 1) % 2

    return c


for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    mask = [int(x) - 1 for x in stdin.readline().split()]
    g = [[] for _ in range(n)]
    degree = [0] * n
    for _ in range(m):
        i, j = [int(x) - 1 for x in stdin.readline().split()]
        g[i].append(j)
        degree[j] += 1

    print(min(search(0), search(1)))
