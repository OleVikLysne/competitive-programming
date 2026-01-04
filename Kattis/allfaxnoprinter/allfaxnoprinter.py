import sys; input=sys.stdin.readline

import heapq

INF = 1 << 60

n, k = map(int, input().split())
size = 2**((n-1).bit_length())

def leq(val, tree):
    i = 1
    while i < size:
        if tree[i*2+1] <= val:
            i = 2*i+1
        else:
            i = 2*i
    return i-size

def update(i, val, tree):
    i += size
    tree[i] = val
    while i != 1:
        i //= 2
        tree[i] = min(tree[2*i], tree[2*i+1])

def naive(jobs, k):
    pq = []
    res = [0]*n
    count = 0
    for start, end, i in jobs:
        while pq and pq[0] <= start:
            heapq.heappop(pq)
        if len(pq) < k:
            count += 1
            heapq.heappush(pq, end)
        res[i] = count
    return res
            

jobs = []
for i in range(n):
    start, time = map(int, input().split())
    jobs.append([start, start+time, i])
naive_res = naive(jobs, k)
jobs.sort(key=lambda x: x[1])
for i in range(n):
    jobs[i].append(i)
jobs.sort(key = lambda x: x[2])


tree = [INF]*(size*2)
cap = 0
count = 0
pq = []
removed = [False]*n
for start, end, i, j in jobs:
    if cap < k:
        update(j, end, tree)
        heapq.heappush(pq, (-end, j))
        cap += 1
        count += 1
    else:
        idx = leq(start, tree)
        if tree[idx+size] <= start:
            removed[idx] = True
            update(idx, INF, tree)
            update(j, end, tree)
            heapq.heappush(pq, (-end, j))
            count += 1
        else:
            while pq:
                x_end, x_j = pq[0]
                x_end = -x_end
                if removed[x_j]:
                    heapq.heappop(pq)
                else:
                    if x_end > end:
                        update(x_j, INF, tree)
                        update(j, end, tree)
                        heapq.heapreplace(pq, (-end, j))
                    break
    sys.stdout.write(f"{count-naive_res[i]} ")
