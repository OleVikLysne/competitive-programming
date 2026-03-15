import sys

input = sys.stdin.readline
from math import sqrt

n, t = map(int, input().split())


def get_pos(t):
    lower, upper = 0, n
    while lower + 1 < upper:
        mid = (lower + upper) // 2
        if positions[mid][0] == t:
            return positions[mid]
        if t < positions[mid][0]:
            upper = mid
        else:
            lower = mid

    x = lower
    if positions[x][0] > t:
        y = x - 1
    else:
        y = x + 1
        x, y = y, x

    vector = [positions[x][1] - positions[y][1], positions[x][2] - positions[y][2]]
    time_diff = positions[x][0] - positions[y][0]
    scale = (t - positions[y][0]) / time_diff

    vector[0] *= scale
    vector[1] *= scale
    return (t, positions[y][1] + vector[0], positions[y][2] + vector[1])


def get_path_length(positions):
    s = 0
    for i in range(len(positions) - 1):
        x1, y1 = positions[i][1:]
        x2, y2 = positions[i + 1][1:]
        s += sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return s


positions = []
for _ in range(n):
    x, y, z = map(int, input().split())
    positions.append((z, x, y))

gps_positions = [get_pos(time) for time in range(0, positions[-1][0], t)]
if gps_positions[-1] != positions[-1]:
    gps_positions.append(positions[-1])
gps_l = get_path_length(gps_positions)
orig_l = get_path_length(positions)
print(((orig_l - gps_l) / orig_l) * 100)
