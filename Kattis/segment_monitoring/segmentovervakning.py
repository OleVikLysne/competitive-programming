import sys; input=sys.stdin.readline
import heapq

x_min, x_max = map(int, input().split())
q = int(input())

singles = set()
start = []
end = []
vandalized = set()

for _ in range(q):
    l = input().split()
    if len(l) == 4:
        s, a, b = int(l[1]), int(l[2]), int(l[3])
        if a <= x_min and x_max <= b:
            singles.add(s)
        else:
            if a <= x_min:
                heapq.heappush(start, (-b, s))
            if x_max <= b:
                heapq.heappush(end, (a, s))
    else:
        s = int(l[1])
        vandalized.add(s)
        singles.discard(s)
    
    if len(singles) > 0:
        print("1")
        continue
    
    while len(start) > 0 and start[0][1] in vandalized:
        heapq.heappop(start)
    while len(end) > 0 and end[0][1] in vandalized:
        heapq.heappop(end)
    
    if not end or not start:
        print("-1")
        continue

    x = -start[0][0]
    y = end[0][0]
    if x >= y:
        print("2")
    else:
        print("-1")
