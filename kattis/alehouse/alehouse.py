n, k = [int(x) for x in input().split()]
events = []
for line in [input().split() for _ in range(n)]:
    a,b = int(line[0]), int(line[1])+k
    events.extend((a, -b))

events.sort(key=lambda x: (abs(x), -x))
max_count, count = 0, 0
for event in events:
    if event >= 0:
        count+=1
    else:
        count-=1
    max_count = max(count, max_count)
print(max_count)
