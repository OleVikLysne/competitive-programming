import sys; input=sys.stdin.readline

MAX = 5*10**5

n, m, z = map(int, input().split())
D = [int(x)-1 for x in input().split()]
V = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
W = [int(x)-1 for x in input().split()]
WORK_DAY = [False]*(MAX+1)
for x in W:
    WORK_DAY[x] = True

D_MAP = [0]*(MAX+1)
W_MAP = [0]*(MAX+1)
j = 0
k = 0
for i in range(MAX+1):
    while j < n and D[j] < i:
        j += 1
    while k < z and W[k] < i:
        k += 1
    D_MAP[i] = j
    W_MAP[i] = k

A = sorted(D+W)
D.append(MAX)
W.append(MAX)

dist = [2**60]*(MAX+1)
dist[D[0]] = 0
if W[0] < D[0]:
    dist[W[0]] = 0

for d in A:
    for i in range(m):
        p = P[i] // 2 if WORK_DAY[d] else P[i]
        v = V[i]
        j = D_MAP[min(d+v, MAX)]
        k = W_MAP[D[j]] - 1
        if k >= 0:
            dist[W[k]] = min(dist[W[k]], dist[d] + p)
        dist[D[j]] = min(dist[D[j]], dist[d] + p)

print(dist[-1])