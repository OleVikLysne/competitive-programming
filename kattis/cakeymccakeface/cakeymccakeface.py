n = int(input())
m = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
occ = {}
for i in range(n):
    for j in range(m):
        diff = b[j]-a[i]
        if diff < 0:
            continue
        occ[diff] = occ.get(diff, 0) + 1
print(max(occ.items(), key=lambda x: (x[1], -x[0]))[0] if len(occ) > 0 else 0)
