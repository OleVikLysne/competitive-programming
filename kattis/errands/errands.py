import sys; input=sys.stdin.readline
from math import sqrt

n = int(input())
coordinates = []
idx_to_place = []
place_to_idx = {}
for i in range(n):
    place, x, y = input().split()
    idx_to_place.append(place)
    place_to_idx[place] = i
    coordinates.append(tuple(map(float, (x, y))))

dist = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        (x1, y1), (x2, y2) = coordinates[i], coordinates[j]
        dist[i][j] = sqrt((x1-x2)**2 + (y1-y2)**2)

HOME = place_to_idx["home"]
WORK = place_to_idx["work"]


def solve(places):
    n = len(places)
    dp = [{} for _ in range(n)]
    for i, pos in enumerate(places):
        dp[0][(1 << i, pos)] = (dist[pos][WORK], (0, WORK))

    for visit_count in range(1, n):
        for i in range(n):
            for key, (distance, _) in dp[visit_count-1].items():
                visited, pos = key
                if visited & (1 << i):
                    continue
                new_visited = visited | (1 << i)
                next_pos = places[i]
                new_distance = distance + dist[pos][next_pos]
                new_key = (new_visited, next_pos)
                if (cur := dp[visit_count].get(new_key)) is None or new_distance < cur[0]:
                    dp[visit_count][new_key] = (new_distance, key)

    shortest_distance = 2**30
    best_key = None
    for key in dp[-1]:
        pos = key[1]
        distance = dp[-1][key][0]
        distance += dist[pos][HOME]
        if distance < shortest_distance:
            shortest_distance = distance
            best_key = key

    path = [-1]*n
    key = best_key
    for i in range(n-1, -1, -1):
        path[i] = key[1]
        key = dp[i][key][1]
    return path


for line in sys.stdin:
    places = [place_to_idx[x] for x in line.split()]
    path = solve(places)
    print(*(idx_to_place[i] for i in path))