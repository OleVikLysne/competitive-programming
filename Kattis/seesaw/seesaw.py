import io, os
Ø = io.BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: next(Ø)
import heapq

n = int(input())

W = [0]*n
P = [0]*n
d = 0
for i in range(n):
    p, w = map(int, input().split())
    d += w*p
    P[i] = p
    W[i] = w

if d > 0:
    i, j = 0, n-1
    while i <= j:
        P[i], P[j] = -P[j], -P[i]
        W[i], W[j] = W[j], W[i]
        i += 1
        j -= 1
    d = -d

heap = [(-W[i], i) for i in range(n)]
heapq.heapify(heap)

S = [1]*n
res = 0
R = [i for i in range(n)]
while d < -1e-7:
    x, i = heapq.heappop(heap)
    if W[i] == 0:
        continue
    p1, w1 = P[i], W[i]
    p2 = (p1 * w1 - d) / w1
    j = R[i]+1
    if j == n:
        res += (p2-p1) * S[i]
        break

    p2 = min(p2, P[j])
    res += (p2-p1) * S[i]
    d += (p2-p1) * W[i]
    R[i] = R[j]
    S[i] += S[j]
    W[i] += W[j]
    P[i] = p2
    W[j] = 0
    heapq.heappush(heap, (-W[i] / S[i], i))

print(res)