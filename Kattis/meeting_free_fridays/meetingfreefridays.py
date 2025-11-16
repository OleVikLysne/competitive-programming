import sys; input=sys.stdin.readline
import bisect

N, T, K = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(N)]
intervals.sort(key=lambda x: x[0])
intervals.append((T, T))

m = [bisect.bisect_left(intervals, intervals[j][1], key = lambda x: x[0]) for j in range(N)]
dp = [[-2**60]*(N+1) for _ in range(N+1)]
dp[0][0] = intervals[0][0]
for i in range(N):
    for j in range(N):
        k = m[j]
        dp[i][j+1] = max(
            dp[i][j+1],
            dp[i][j] + intervals[j+1][0] - intervals[j][0]
        )
        dp[i+1][k] = max(
            dp[i+1][k],
            dp[i][j] + intervals[k][0] - intervals[j][1]
        )
for i in range(N, -1, -1):
    if dp[i][N] >= K:
        print(i)
        break
