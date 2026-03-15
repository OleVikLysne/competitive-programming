import sys; input=sys.stdin.readline

def impossible():
    print("impossible")
    exit()
def possible():
    print("possible")
    exit()

n, q, s = map(int, input().split())
sensors = [int(x)-1 for x in input().split()]
capacities = [int(x) for x in input().split()]
windows = []
mbs = [0]*n
for t in range(n):
    probes = [0]*q
    line = [int(x) for x in input().split()]
    mb = line[0]
    mbs[t] = mb
    for i, x in enumerate(line[1:]):
        probes[sensors[i]] += x
    windows.append(probes)


total_probe = [0]*q
max_at_time = [[0]*q for _ in range(n+1)]
min_at_time = [[0]*q for _ in range(n+1)]
restrictions = []

for t in range(n):
    probes = windows[t]
    for i in range(q):
        total_probe[i] += probes[i]
        max_at_time[t][i] = total_probe[i]
        min_at_time[t][i] = max(0, total_probe[i] - capacities[i])
        if min_at_time[t][i] > 0 and (t == 0 or min_at_time[t-1][i] < min_at_time[t][i]):
            restrictions.append((t, i))

for i in range(q):
    if total_probe[i] > 0 and min_at_time[n-1][i] < total_probe[i]:
        restrictions.append((n, i))
        min_at_time[n][i] = total_probe[i]

restrictions.reverse()

sent_data = [0]*q
for t0 in range(n):
    mb = mbs[t0]
    for j in range(len(restrictions)-1, -1, -1):
        if mb == 0:
            break
        t1, i = restrictions[j]
        if t1 < t0+1:
            impossible()
        min_diff = min_at_time[t1][i] - sent_data[i]
        max_diff = max_at_time[t0][i] - sent_data[i]
        x = min(mb, min_diff, max_diff)
        if x == 0:
            continue
        if x == min_diff:
            restrictions.pop(j)
        sent_data[i] += x
        mb -= x

if restrictions:
    impossible()
possible()