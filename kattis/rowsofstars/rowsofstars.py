import io, os
Ø = io.BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: next(Ø)
from collections import deque

INF = 2**60

n, k, d, s = map(int, input().split())
arr = [int(input()) for _ in range(n)]
t = [0]*n
t[0] = sum(arr[:s])
for i in range(n-1):
    t[i+1] = t[i] - arr[i] + arr[(i+s)%n]

tot = [INF]*n
for i in range(n):
    if tot[i] != INF:
        continue
    x = t[i]
    j = (i + k) % n
    c = 1
    while c < d:
        if j == i and (m := d // c) > 1:
            c *= m
            x *= m
        else:
            x += t[j]
            j = (j + k) % n
            c += 1
    while tot[i] == INF:
        tot[i] = x
        x -= t[i]
        x += t[j]
        i = (i + k) % n
        j = (j + k) % n


visit_row = [INF]*n
q = deque([i for i in range(n-s+1)])
for i in range(n-s+1):
    visit_row[i] = 0

res = -INF
while q:
    i = q.popleft()
    res = max(res, tot[i])
    j = (i + k) % n
    row = visit_row[i] + 1
    if row < visit_row[j] and row <= n-d:
        visit_row[j] = row
        q.append(j)
print(res)