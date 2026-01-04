import sys; input=sys.stdin.readline
import heapq

MAX = 2**62
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])
arr.append((MAX, MAX, MAX))

def solve(k):
    heap = []
    i = 0
    day = 0
    while i < n or heap:
        if not heap:
            day = arr[i][0]
        while i < n and arr[i][0] == day:
            heapq.heappush(heap, (arr[i][1], arr[i][2]))
            i += 1
        next_day = min(heap[0][0]+1, arr[i][0])
        T = k * (next_day - day)
        day = next_day
        while heap:
            deadline, t = heap[0]
            if T < t:
                if deadline < day:
                    return False
                heapq.heapreplace(heap, (deadline, t-T))
                break
            heapq.heappop(heap)
            T -= t
    return True

l, r = 0, MAX
while l < r:
    mid = (l+r)//2
    if not solve(mid):
        l = mid + 1
    else:
        r = mid
print(l)
