from math import log
while input() != "0":
    currencies = input().split()
    C = len(currencies)
    index_map = {x : i for i, x in enumerate(currencies)}
    dist = [[float("inf") for _ in range(C)] for _ in range(C)]
    R = int(input())
    for _ in range(R):
        c1, c2, rate = input().split()
        r1, r2 = [int(x) for x in rate.split(":")]
        w = log(r1/r2)
        c1, c2 = index_map[c1], index_map[c2]
        dist[c1][c2] = w

    for i in range(C):
        dist[i][i] = 0

    
    for k in range(C):
        for j in range(C):
            for i in range(C):
                val = dist[i][k] + dist[k][j]
                if dist[i][j] > val:
                    dist[i][j] = val
                    if i == j and val < 0:
                        print("Arbitrage")
                        break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print("Ok")



# from math import log

# def bellman_ford(s):
#     dist, pred = {v: float("inf") for v in range(C)}, {}
#     dist[s] = 0
#     for _ in range(C-1):
#         for parent in range(C):
#             for (child, w) in G[parent]:
#                 if dist[child] > dist[parent] + w:
#                     dist[child] = dist[parent] + w
#                     pred[child] = parent
                

#     for parent in range(C):
#         for (child, w) in G[parent]:
#             if dist[child] > dist[parent] + w:
#                 return True
#     removal = set()
#     for v, val in dist.items():
#         if val < float("inf"):
#             removal.add(v)
#     return removal

# while input()!="0":
#     currencies = input().split()
#     C = len(currencies)
#     index_map = {x : i for i, x in enumerate(currencies)}
#     G = [[] for _ in range(C)]

#     R = int(input())

#     for _ in range(R):
#         c1, c2, rate = input().split()
#         r1, r2 = [int(x) for x in rate.split(":")]
#         w = log(r1/r2)
#         c1, c2 = index_map[c1], index_map[c2]
#         G[c1].append((c2, w))
    
#     candidates = set([x for x in range(C)])
#     while candidates:
#         run = bellman_ford(candidates.__iter__().__next__())
#         if run is True:
#             print("Arbitrage")
#             break
#         candidates -= run
#     else:
#         print("Ok")
