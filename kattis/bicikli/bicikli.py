import sys; input=sys.stdin.readline
sys.setrecursionlimit(2**30)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
rev_g = [[] for _ in range(n)]
roots = set(range(n))
for _ in range(m):
    u, v = (int(x)-1 for x in input().split())
    g[u].append(v)
    rev_g[v].append(u)
    roots.discard(v)
    
if not roots:
    print("inf")
    exit()


can_reach = [False]*n
def search(v):
    can_reach[v] = True
    for u in rev_g[v]:
        if not can_reach[u]:
            search(u)
search(1)

if not can_reach[0]:
    print(0)
    exit()


rec_visited = [False]*n
mem = [-1]*n
def dfs(v):
    if v == 1:
        return 1
    if mem[v] != -1:
        return mem[v]
    rec_visited[v] = True
    total = 0
    for u in g[v]:
        if not can_reach[u]:
            continue
        if rec_visited[u]:
            print("inf")
            exit()
        total += dfs(u)
    mem[v] = total
    rec_visited[v] = False
    return total

res = str(dfs(0))[-9:]
print(res)