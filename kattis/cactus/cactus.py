import sys; input=sys.stdin.readline
sys.setrecursionlimit(2**30)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)

def fully_connected(g):
    def _all_reachable(g):
        visited = [False]*n
        stack = [0]
        visited[0] = True
        while stack:
            v = stack.pop()
            for u in g[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)

        return all(visited)
    
    g2 = [[] for _ in range(n)]
    for v in range(n):
        for u in g[v]:
            g2[u].append(v)
    
    return _all_reachable(g) and _all_reachable(g2)

if not fully_connected(g):
    print("NO")
    exit()

cycle = set()
def add(u, v):
    if (u, v) in cycle:
        print("NO")
        exit()
    cycle.add((u, v))

stack = []
on_stack = [False]*n
def dfs(v):
    if on_stack[v]:
        u = v
        i = len(stack)-1
        while True:
            w = stack[i]
            add(w, u)
            u = w
            i -= 1
            if u == v:
                break
        return

    on_stack[v] = True
    stack.append(v)
    for u in g[v]:
        dfs(u)
    on_stack[v] = False
    stack.pop()

dfs(0)
print("YES" if len(cycle) == m else "NO")