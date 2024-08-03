import sys; input=sys.stdin.readline
from math import sqrt

n = int(input())
coordinates = []
idx_to_place = []
place_to_idx = {}
for _ in range(n):
    place, x, y = input().split()
    place_to_idx[place] = len(idx_to_place)
    coordinates.append(tuple(map(float, (x, y))))
    idx_to_place.append(place)

dist = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        (x1, y1), (x2, y2) = coordinates[i], coordinates[j]
        dist[i][j] = sqrt((x1-x2)**2 + (y1-y2)**2)

home = place_to_idx["home"]
work = place_to_idx["work"]

DEFAULT = (float("inf"), (float("inf"), float("inf")))

def solve(dp, places):
    for visit_count in range(1, len(dp)):
        for next_pos in places:
            for key in dp[visit_count-1]:
                visited, pos = key
                if visited & (1 << next_pos):
                    continue
                distance, _ = dp[visit_count-1][key]
                new_distance = distance + dist[pos][next_pos]
                new_visited = visited | (1 << next_pos)
                new_key = (new_visited, next_pos)
                dp[visit_count][new_key] = min(dp[visit_count].get(new_key, DEFAULT), (new_distance, key))


    shortest_distance = float("inf")
    for key in dp[-1]:
        pos = key[1]
        distance, _ = dp[-1][key]
        distance += dist[pos][home]
        if distance < shortest_distance:
            shortest_distance = distance
            best_key = key

    path = [-1]*len(dp)
    key = best_key
    for i in range(len(dp)-1, -1, -1):
        path[i] = key[1]
        _, key = dp[i][key]
    return path



for line in sys.stdin:
    places = [place_to_idx[x] for x in line.split()]
    dp = [{} for _ in range(len(places))]
    for i in places:
        dp[0][(1 << i, i)] = (dist[i][work], (0, work))
    path = solve(dp, places)
    print(" ".join(idx_to_place[i] for i in path))