import sys; input=sys.stdin.readline
from math import ceil
from collections import defaultdict

m = {
    1:100,
    2:75,
    3:60,
    4:50,
    5:45,
    6:40,
    7:36,
    8:32,
    9:29,
    10:26,
    11:24,
    12:22,
    13:20,
    14:18,
    15:16
}
score_map = defaultdict(int)
for k, v in m.items():
    score_map[k] = v

for i in range(16, 31):
    score_map[i] = 31 - i

n = int(input())
l = []
scores = [0]*n
for i in range(n):
    s, p, f, o = map(int, input().split())
    scores[i] = o
    l.append((-s, p, f, i))
l.sort()


for i in range(n):
    c = 1
    s = score_map[i+1]
    for j in range(i-1, -1, -1):
        if l[i][:3] != l[j][:3]:
            break
        s += score_map[j+1]
        c += 1
    for j in range(i+1, n):
        if l[i][:3] != l[j][:3]:
            break
        s += score_map[j+1]
        c += 1
    if i >= 30 and c == 1:
        break

    scores[l[i][-1]] += ceil(s/c)


print(*scores)
