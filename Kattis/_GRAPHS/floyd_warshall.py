def floyd_warshall(dist: list[list[int]]):
    n = len(dist)
    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for j in range(n):
            for i in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


    # the following is possibly necessary if we the graph has negative cycles
    for i in range(n):
        for j in range(n):
            if dist[i][j] == -float("inf"):
                continue
            for k in range(n):
                if dist[i][k] != float("inf") and dist[k][j] != float("inf") and dist[k][k] < 0:
                    dist[i][j] == -float("inf")
    return dist