import sys; input=sys.stdin.readline

n, k, c = map(int, input().split())
idx_to_name = [input().rstrip() for _ in range(n)]
name_to_idx = {x: i for i, x in enumerate(idx_to_name)}
enemies = [0]*n
f = lambda x: name_to_idx[x]
for _ in range(k):
    a, b = map(f, input().split())
    enemies[a] |= 1 << b
    enemies[b] |= 1 << a

best_buses = [None]*(n+1)
def search(i, buses):
    global best_buses
    if i == n:
        if len(best_buses) > len(buses):
            best_buses = [x[1] for x in buses]
        return

    for j in range(len(buses)):
        if len(buses) >= len(best_buses):
            return
        if buses[j][0] == c:
            continue
        if buses[j][1] & enemies[i]:
            continue
        buses[j][0] += 1
        buses[j][1] |= 1 << i
        search(i+1, buses)
        buses[j][1] ^= 1 << i
        buses[j][0] -= 1

    if len(buses)+1 >= len(best_buses):
        return
    buses.append([1, 1 << i])
    search(i+1, buses)
    buses.pop()

search(0, [])
print(len(best_buses))
for mask in best_buses:
    print(" ".join(idx_to_name[i] for i in range(n) if mask & 1 << i))
