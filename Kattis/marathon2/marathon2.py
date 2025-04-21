import sys; input=sys.stdin.readline
import heapq, math


n, x, y = map(int, input().split())
r, j = map(int, input().split())
scale = math.lcm(r, j) # scale the calcuations by lcm to avoid floating point WA

MAX = 42_195 * scale
x *= scale
y *= scale

stations = {p for _ in range(n) if (p := int(input())*scale) < MAX}
stations.add(MAX)
stations.add(0)
stations = sorted(stations)
n = len(stations)

def bin_search(i, w):
    l, r = i+1, n-1
    while l+1 < r:
        mid = (l+r)//2
        d = stations[mid] - stations[i]
        if d <= w:
            l = mid
        else:
            r = mid
    return l

def solve():
    heap = [(0, 0, x)]
    max_w = [-1]*n
    res = 2**60
    while heap:
        t, i, w = heapq.heappop(heap)
        if max_w[i] >= w:
            continue
        max_w[i] = w

        idx = bin_search(i, w)
        for k in (idx, idx+1, n-1):
            if k == n: continue
            d = stations[k] - stations[i]
            jog_d = max(0, d - w)
            run_d = d - jog_d
            next_w = max(0, w - d)
            next_t = t + jog_d // j + run_d // r
            if k == n-1:
                res = min(res, next_t)
                continue
            if next_t < res:
                heapq.heappush(heap, (next_t, k, next_w))
            if next_t + y < res:
                heapq.heappush(heap, (next_t+y, k, x))
    return res

time = solve()
time //= scale # convert back to un-scaled time
h, s = divmod(time, 3600)
m, s = divmod(s, 60)
print("{:02d}:{:02d}:{:02d}".format(h, m, s))