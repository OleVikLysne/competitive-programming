import sys; input=sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

comp = [-1]*n
for i in range(n):
    if comp[i] == -1:
        stack = [i]
        comp[i] = i
        while stack:
            v = stack.pop()
            for u in g[v]:
                if comp[u] != comp[v]:
                    comp[u] = comp[v]
                    stack.append(u)
            

visited1 = [-1]*n
visited2 = [-1]*n
dist1 = [-1]*n
dist2 = [-1]*n
for i in range(int(input())):
    a, b = map(int, input().split())
    if comp[a] != comp[b]:
        print(-1)
        continue
    
    q1 = deque([(a, 0)])
    q2 = deque([(b, 0)])
    visited1[a] = i
    visited2[b] = i
    dist1[a] = 0
    dist2[b] = 0
    prev1 = prev2 = 0
    while q1 or q2:
        if prev1 != q1[0][1]:
            prev1 = q1[0][1]
            q1, dist1, visited1, prev1, q2, dist2, visited2, prev2 = q2, dist2, visited2, prev2, q1, dist1, visited1, prev1
        v, d = q1.popleft()
        for u in g[v]:
            if visited1[u] == i:
                continue
            if visited2[u] == i:
                print(d + 1 + dist2[u])
                break
            dist1[u] = d + 1
            visited1[u] = i
            q1.append((u, d+1))
        else:
            continue
        break
