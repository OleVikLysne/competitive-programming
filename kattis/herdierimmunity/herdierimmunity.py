import sys; input=sys.stdin.readline
import heapq

NEG_INF = -2**60
n, m = map(int, input().split())
arr = [int(x) for x in input().split()]

one_sided = [-(arr[0]-1), -(n-arr[-1])]
two_sided = [-(arr[i+1]-arr[i]-2) for i in range(m-1)]
heapq.heapify(one_sided)
heapq.heapify(two_sided)
count = 0
t = 0
while one_sided or two_sided:
    td = -two_sided[0] - t*2 if two_sided else NEG_INF
    od = -one_sided[0] - t if one_sided else NEG_INF
    if td < 0 and od < 0:
        break
    if td > od:
        count += 1
        heapq.heappop(two_sided)
        heapq.heappush(one_sided, -(td+t))
    else:
        count += od
        heapq.heappop(one_sided)
    t += 1
print(count)