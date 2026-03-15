import sys; input=sys.stdin.readline
from collections import deque
n = int(input())
start = [0]
arr = [int(input()) for _ in range(n)]
for i in range(1, n):
    if arr[i] >= arr[start[0]]:
        if arr[i] > arr[start[0]]:
            start.clear()
        start.append(i)

res = [-1]*n

m = [[-1, -1] for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            m[i][0] = j
            break
        k = m[j][0]
        if k == -1 or arr[k] > arr[i]:
            m[i][0] = k
            break


for i in range(n):
    for j in range(i-1, -1, -1):
        if arr[j] > arr[i]:
            m[i][1] = j
            break
        k = m[j][1]
        if k == -1 or arr[k] > arr[i]:
            m[i][1] = k
            break

rev_m = [[] for _ in range(n)]
for i in range(n):
    for j in m[i]:
        if j == -1:
            continue
        rev_m[j].append(i)


q = deque([(x, 0) for x in start])
for i in start:
    res[i] = 0
while q:
    i, c = q.popleft()
    for j in rev_m[i]:
        if res[j] == -1:
            res[j] = c+1
            q.append((j, c+1))
print(*res)
