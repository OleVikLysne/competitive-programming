n, k = map(int, input().split())
g = [-1 for _ in range(n)]
rev_g = [[] for _ in range(n)]
for i, x in enumerate(map(lambda y: int(y)-1, input().split())):
    g[i] = x
    rev_g[x].append(i)

def cycle_detect(g: list[list[int]]):
    n = len(g)
    rec_visited = [False]*n
    visited = [False]*n
    path = []
    cycles = []
    def get_cycle(path, v):
        u = path[-1]
        cycle = [u]
        i = len(path)-2
        while u != v and i >= 0:
            u = path[i]
            cycle.append(u)
            i -= 1
        return cycle

    def dfs(v):
        rec_visited[v] = True
        visited[v] = True
        path.append(v)
        u = g[v]
        if rec_visited[u]:
            cycles.append(get_cycle(path, u))
        elif not visited[u]:
            dfs(u)
        path.pop()
        rec_visited[v] = False

    for v in range(n):
        if not visited[v]:
            dfs(v)

    return cycles

cycles = cycle_detect(g)

rec_visit = [False]*n
def reachable(v):
    if rec_visit[v]:
        return 0
    s = 1
    rec_visit[v] = True
    for u in rev_g[v]:
        s += reachable(u)
    rec_visit[v] = False
    return s


minimaxi = []
for cyc in cycles:
    rep = cyc[0]
    if len(cyc) == 1 and g[rep] != rep:
        continue
    minimaxi.append((len(cyc), reachable(rep)+1))


def knapsack(k):
    possible = [False]*(k+1)
    possible[0] = True
    for lower, upper in minimaxi:
        for j in range(k-lower, -1, -1):
            if possible[j]:
                for w in range(lower, upper):
                    if j+w > k:
                        break
                    possible[j+w] = True
            
    for j in range(k, -1, -1):
        if possible[j]:
            return j
    return 0


print(knapsack(k))
