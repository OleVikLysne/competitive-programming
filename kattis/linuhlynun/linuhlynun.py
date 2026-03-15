import sys; input=sys.stdin.readline

n = int(input())

arr = sorted((tuple(map(int, input().split())) for _ in range(n)), key = lambda x: x[0])
mini = 0
a = arr[0][0]
ahead = 0
behind = arr[0][1]
best = a
for i in range(1, n):
    x, c = arr[i]
    mini += (x-a)*c
    ahead += c

total = mini
prev = a
for i in range(1, n):
    x, c = arr[i]
    dist = (x-prev)
    total += behind*dist
    total -= ahead*dist
    behind += c
    ahead -= c
    if total < mini:
        best = x
        mini = total
    prev = x
print(best)
