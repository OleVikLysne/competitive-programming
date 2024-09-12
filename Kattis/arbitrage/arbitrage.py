import sys; input=sys.stdin.readline; print=sys.stdout.write
from math import log
INF = float("inf")
ARBITRAGE = "Arbitrage "
OK = "Ok "

def floyd_warshall(dist):
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for j in range(n):
            for i in range(n):
                val = dist[i][k] + dist[k][j]
                if dist[i][j] > val:
                    dist[i][j] = val
                    if i == j and val < 0:
                        return ARBITRAGE
    return OK

while (n := int(input())) != 0:
    index_map = {x : i for i, x in enumerate(input().split())}
    dist = [[INF]*n for _ in range(n)]
    for _ in range(int(input())):
        c1, c2, rate = input().split()
        r1, r2 = map(int, rate.split(":"))
        c1, c2 = index_map[c1], index_map[c2]
        dist[c1][c2] = log(r1/r2)

    print(floyd_warshall(dist))