import sys; input = sys.stdin.readline

n, m = map(int, input().split())
name_to_idx = {}
idx_to_name = input().split()
for i, x in enumerate(idx_to_name):
    name_to_idx[x] = i
hunter = [False]*n
hunter[0] = True
cheat = set()
for _ in range(m):
    l = input().split()
    a, b = name_to_idx[l[0]], name_to_idx[l[2]]
    if not hunter[a]:
        cheat.add(a)
    else:
        hunter[a] = False
    hunter[b] = True
print(len(cheat))
print(*sorted(idx_to_name[a] for a in cheat))
