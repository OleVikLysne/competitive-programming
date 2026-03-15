from sys import stdin

n, m = map(int, stdin.readline().split())
g = [[] for _ in range(n)]
solo = set(range(n))
a = float("inf")
for _ in range(m):
    i, j = [int(x)-1 for x in stdin.readline().split()]
    g[i].append(j)
    g[j].append(i)
    if i in solo: solo.remove(i)
    if j in solo: solo.remove(j)
    a = min(min(a, i), j)

for i in solo:
    g[i].append(a)
    g[a].append(i)

add_cycle = True

# def dfs(v, color=0):
#     global add_cycle
#     coloring[v] = color
#     color = (color + 1) % 2
#     to_visit.remove(v)
#     for u in g[v]:
#         if coloring[u] == -1:
#             dfs(u, color)
#         elif coloring[u] != color:
#             add_cycle = False


def dfs(v):
    global add_cycle
    stack = [(v, 0)]
    while stack:
        v, color = stack.pop()
        coloring[v] = color
        color = (color + 1) % 2
        for u in g[v]:
            if u in to_visit:
                to_visit.remove(u)
                stack.append((u, color))
            elif coloring[u] != color and coloring[u] != -1:
                add_cycle = False
        


s = len(solo)
coloring = [-1]*n
to_visit = set(range(n))
while to_visit:
    v = to_visit.__iter__().__next__()
    to_visit.remove(v)
    dfs(v)
    if to_visit:
        s += 1

if add_cycle:
    s += 1
print(s)
