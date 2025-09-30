import sys; input=sys.stdin.readline
import heapq
import bisect

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, w))
    g[v].append((u, w))


dist = [[2**60]*n for _ in range(n)]
for source in range(n):
    dist[source][source] = 0
    for v in range(source):
        dist[source][v] = dist[v][source]
    pq = [(dist[source][v], v) for v in range(source+1)]
    heapq.heapify(pq)
    while pq:
        _, v = heapq.heappop(pq)
        for u, w in g[v]:
            if dist[source][u] > dist[source][v]+w:
                dist[source][u] = dist[source][v]+w
                heapq.heappush(pq, (dist[source][u], u))

k = int(input())
ready = [0]*k
node = [0]*k
placed = [0]*k
for i in range(k):
    s, u, t = map(int, input().split())
    u -= 1
    placed[i] = s
    ready[i] = t
    node[i] = u

def pack(i, j, v):
    x = j*k+i
    y = x*n+v
    return y

def unpack(y):
    x, v = divmod(y, n)
    j, i = divmod(x, k)
    return i, j, v

INF = 2**60

def solve(d):
    mem = [[[INF]*2 for _ in range(k+1)] for _ in range(k)]
    mem[0][0][0] = 0
    for i in range(k):
        for j in range(i+1, k+1):
            mem[i][j][0] = min(
                mem[i][j][0],
                mem[i][j-1][0]
            )
            if i > 0:
                mem[i][j][0] = min(
                    mem[i][j][0],
                    mem[i-1][j][1] + dist[node[i-1]][0],
                )
            mem[i][j][0] = max(
                mem[i][j][0],
                ready[j-1]
            )
            mem[i][j][1] = mem[i][j][0] + dist[0][node[i]]
            if i > 0:
                mem[i][j][1] = min(
                    mem[i][j][1],
                    mem[i-1][j][1] + dist[node[i-1]][node[i]],
                )

            if mem[i][j][1] - placed[i] > d:
                mem[i][j][1] = INF
    
    for i in range(k):
        print(mem[i])
    print()

    return mem[k-1][k][1] - placed[k-1] <= d

mem = [[[INF]*2 for _ in range(k+1)] for _ in range(k)]
visit = [[[-1]*2 for _ in range(k+1)] for _ in range(k)]
mem[0][1][0] = ready[0]
def solve2(d):
    heap = [(ready[0], pack(0, 1, 0))]
    while heap:
        t, y = heapq.heappop(heap)
        i, j, v = unpack(y)
        l = 0 if v == 0 else 1
        if mem[i][j][l] < t:
            continue
        if i == k-1 and node[i] == v:
            return True
        
        ni = (i+1) if node[i] == v else i
        if ni < j and (nt := t + dist[v][node[ni]]) - placed[ni] <= d:
            nj = j
            if mem[ni][nj][1] > nt or visit[ni][nj][1] != d:
                visit[ni][nj][1] = d
                mem[ni][nj][1] = nt
                heapq.heappush(heap, (nt, pack(ni, nj, node[ni])))
        
        if j < k and (nt := t + dist[v][0]) - placed[ni] <= d:
            if v == 0:
                nt = ready[j]
                if nt - placed[ni] > d:
                    continue
                nj = j + 1
            else:
                nj = bisect.bisect_right(ready, nt)
            if visit[ni][nj][0] != d or (mem[ni][nj][0] > nt and mem[ni][nj][1] > t):
                visit[ni][nj][0] = d
                mem[ni][nj][0] = nt
                heapq.heappush(heap, (nt, pack(ni, nj, 0)))

    return False




# lo, hi = 1, 2**60
# while lo < hi:
#     mi = (lo+hi)//2
#     if solve(mi):
#         hi = mi
#     else:
#         lo = mi + 1
# print(lo)

solve(7)
solve2(7)
for i in range(k):
    print(mem[i])