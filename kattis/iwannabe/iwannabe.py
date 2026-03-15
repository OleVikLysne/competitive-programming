import sys; input=sys.stdin.readline
from copy import deepcopy

n, k = map(int, input().split())
attack = [(i, *map(int, input().split())) for i in range(n)]
defense = deepcopy(attack)
health = deepcopy(attack)

attack.sort(key=lambda x: x[1])
defense.sort(key=lambda x: x[2])
health.sort(key=lambda x: x[3])

visited = [False]*n
s = 0
for arr in (attack, defense, health):
    for _ in range(k):
        i = arr.pop()[0]
        if visited[i]:
            continue
        s += 1
        visited[i] = True

print(s)
