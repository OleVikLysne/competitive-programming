n, b = map(int, input().split())
if n == 1:
    print(1)
    exit()

def brute_force(i):
    values = [fights[a][0] for a in range(n) if a != i]
    j = n-2
    k = n-3
    while k >= 0:
        diff = min(values[j], values[k])
        values[j] -= diff
        values[k] -= diff
        while j > 0 and values[j] <= 0:
            j -= 1
        k -= 1

    if values[j] > fights[i][0]:
        return 2
    return 1

fights = [(-(-int(x)//b), i) for i, x in enumerate(input().split())]
fights.sort()
lower, upper = 0, n
while lower+1 < upper:
    mid = (lower+upper)//2
    if brute_force(mid) == 2:
        lower = mid
    else:
        upper = mid

while lower < n and brute_force(lower) == 2:
    lower += 1

res = [0]*n
for j, (_, i) in enumerate(fights):
    if j >= lower:
        res[i] = 1
    else:
        res[i] = 2
print(*res)
