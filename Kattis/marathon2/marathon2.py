import sys; input=sys.stdin.readline

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

jump = [-1]*n
k = 0
for i in range(n-1):
    while k < n-1 and stations[k] - stations[i] <= x:
        k += 1
    jump[i] = k

dp = [2**60]*n
dp[0] = 0
for i in range(n-1):
    for k in (jump[i]-1, jump[i], n-1):
        if k == i: continue
        d = stations[k] - stations[i]
        run_d = min(d, x)
        jog_d = d - run_d
        next_t = dp[i] + jog_d // j + run_d // r
        if k != n-1:
            next_t += y
        dp[k] = min(dp[k], next_t)

res = dp[-1]
res //= scale # convert back to un-scaled time
h, s = divmod(res, 3600)
m, s = divmod(s, 60)
print("{:02d}:{:02d}:{:02d}".format(h, m, s))