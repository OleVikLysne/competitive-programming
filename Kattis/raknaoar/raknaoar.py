import sys; input=sys.stdin.readline
import heapq

n, q = map(int, input().split())
C = [0]*n
islands = []
for i in range(n):
    x = map(int, input().split())
    C[i] = next(x)
    islands.extend((a, i) for a in x)

islands.sort(key=lambda x: x[0], reverse=True)
Q = list(map(lambda i: (i, int(input())), range(q)))
Q.sort(key=lambda x: x[1])
heap = [(-C[i], -i) for i in range(n)]
heapq.heapify(heap)
res = [0]*q
for j, a in Q:
    while islands and islands[-1][0] < a:
        _, i = islands.pop()
        C[i] -= 1

    while True:
        c, i = heap[0]
        x = -C[-i]
        if x == c:
            break
        heapq.heappushpop(heap, (x, i))
    res[j] = -heap[0][1] + 1

print("\n".join(map(str, res)))