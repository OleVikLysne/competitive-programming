import sys; input=sys.stdin.readline
n, k = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
MAX = 100_000
T = min(int(input()), MAX)

sss = [-1]*(T+1)
sss[0] = 0
res = 0
for l, d in arr:
    for i in range(T, -1, -1):
        v = sss[i]
        sss[i] = -1
        if v != -1:
            if i+k <= T:
                sss[i+k] = max(sss[i+k], v)
            if i+l <= T:
                sss[i+l] = max(sss[i+l], v+d)
                res = max(res, sss[i+l])
print(res)