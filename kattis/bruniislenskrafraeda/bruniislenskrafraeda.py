import sys; input=sys.stdin.readline

n, T = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
time = 0

arr.sort(key = lambda x: x[0], reverse=True)
for i in range(n-1, -1, -1):
    t, f = arr[i]
    if t > T:
        break
    if t > f:
        continue
    arr[i], arr[-1] = arr[-1], arr[i]
    arr.pop()
    T += f-t
    time += t

arr.sort(key = lambda x: x[1], reverse=True)
dp = [T-x for x in range(T+1)]
for t, f in arr:
    for i in range(t, T+1):
        dp[i-t+f] = max(dp[i-t+f], dp[i] + t)

r = 0
for i in range(T+1):
    r = max(r, dp[i] + i)

print(r + time)