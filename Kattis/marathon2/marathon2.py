import sys; input=sys.stdin.readline

INF = 2**60

n, x, y = map(int, input().split())
r, j = map(int, input().split())
scale = r*j # scale to avoid floating point
x *= scale
y *= scale

stations = {int(input())*scale for _ in range(n)}
stations.add(42_195 * scale)
stations.add(0)
stations = sorted(stations)
n = len(stations)

dp = [INF]*n
dp[0] = 0
idx = 0
for i in range(n-1):
    if dp[i] == INF: continue
    while idx < n-2 and stations[idx] - stations[i] <= x:
        idx += 1
    for k in (idx-1, idx, n-1):
        d = stations[k] - stations[i]
        run_d = min(d, x)
        jog_d = d - run_d
        next_t = dp[i] + jog_d // j + run_d // r + y
        dp[k] = min(dp[k], next_t)

res = dp[-1] - y
res //= scale # convert back to un-scaled time
h, s = divmod(res, 3600)
m, s = divmod(s, 60)
print("{:02d}:{:02d}:{:02d}".format(h, m, s))