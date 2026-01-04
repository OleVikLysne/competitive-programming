import sys
import math
sys.setrecursionlimit(2**30)


INF = 1 << 30
dist = [-1] * 100_001
dist[1] = 1
s = input()

def solve(s):
    if s[0] == "0":
        return INF
    n = int(s)
    if dist[n] != -1:
        return dist[n]
    res = INF
    for i in range(1, len(s)):
        res = min(res, solve(s[:i]) + solve(s[i:]))

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res = min(res, solve(str(i)) + solve(str(n // i)))

    for i in range(1, min(n, 101)):
        res = min(res, solve(str(i)) + solve(str(n - i)))
    dist[n] = res
    return res

print(solve(s))
