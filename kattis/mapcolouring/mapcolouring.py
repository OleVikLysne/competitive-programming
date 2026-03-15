import sys; input=sys.stdin.readline

def solve(v, c, color):
    if v == n:
        return True
    for o in set(range(c)) - {color[u] for u in g[v]}:
        color[v] = o
        if solve(v+1, c, color):
            return True
        color[v] = -1
    return False

for _ in range(int(input())):
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    for c in range(1, 5):
        color = [-1]*n
        if solve(0, c, color):
            print(c)
            break
    else:
        print("many")
