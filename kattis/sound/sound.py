import sys; input = sys.stdin.readline
import heapq


n, m, c = map(int, input().split())
recording = [int(x) for x in input().split()]

min_pq = [(x, i) for i, x in enumerate(recording[:m])]
max_pq = [(-x, i) for i, x in enumerate(recording[:m])]
heapq.heapify(min_pq)
heapq.heapify(max_pq)

found = False
for i in range(n - m + 1):
    j = min_pq[0][1]
    while i > j:
        heapq.heappop(min_pq)
        j = min_pq[0][1]

    k = max_pq[0][1]
    while i > k:
        heapq.heappop(max_pq)
        k = max_pq[0][1]

    maxi = -max_pq[0][0]
    mini = min_pq[0][0]

    if maxi - mini <= c:
        print(i + 1)
        found = True

    if i < n - m:
        heapq.heappush(min_pq, (recording[i + m], i + m))
        heapq.heappush(max_pq, (-recording[i + m], i + m))

if not found:
    print("NONE")
