import sys; input=sys.stdin.readline
from collections import deque

n, D = map(int, input().split())
infected = map(lambda x: int(x)-1, input().split()[1:])
enter, exit = [], []
for i in range(n):
    a, b = map(int, input().split())
    enter.append((a, i))
    exit.append((b, i))

enter.sort(reverse=True)
exit.sort(reverse=True)

g = [[] for _ in range(n)]
in_room = set()
while enter:
    if exit[-1][0] < enter[-1][0]:
        in_room.remove(exit.pop()[1])
        continue
    i = enter.pop()[1]
    for j in in_room:
        g[j].append(i)
        g[i].append(j)
    in_room.add(i)


q = deque((0, v) for v in infected)
res= set()
depth = [None]*n
while q:
    d, v = q.popleft()
    if d > D:
        break
    res.add(v+1)
    for u in g[v]:
        if depth[u] is None:
            depth[u] = d + 1
            q.append((depth[u], u))

print(*sorted(res))