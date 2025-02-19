import sys; input=sys.stdin.readline
import math
n, q = map(int, input().split())
thresh = int(math.sqrt(n))
sq = [[0]*thresh for _ in range(thresh)]
arr = [0]*(n+1)
for _ in range(q):
    t, *query = input().split()
    if t == "1":
        a, b, c = map(int, query)
        if b < thresh:
            sq[b][a] += c
        else:
            while a <= n:
                arr[a] += c
                a += b
    else:
        i = int(query[0])
        ans = arr[i]
        for k in range(1, thresh):
            ans += sq[k][i % k]
        sys.stdout.write(f"{ans} ")
