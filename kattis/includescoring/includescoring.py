import sys; input=sys.stdin.readline
from math import ceil

SCORE_MAP = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16]
SCORE_MAP.extend(range(15, 0, -1))

n = int(input())
l = []
scores = [0]*n
for i in range(n):
    s, p, f, o = map(int, input().split())
    scores[i] += o
    l.append(((-s, p, f), i))
l.sort()

j = 0
for i in range(n):
    if j == i:
        if i >= 30:
            break
        while j < n and l[i][0] == l[j][0]:
            j += 1
        cur_score = 0
        for k in range(i, min(30, j)):
            cur_score += SCORE_MAP[k]
        cur_score = ceil(cur_score/(j-i))
    scores[l[i][1]] += cur_score

print(*scores)
