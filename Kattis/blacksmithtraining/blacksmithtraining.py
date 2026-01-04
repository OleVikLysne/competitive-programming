import sys; input = sys.stdin.readline
n = int(input())
plans = [tuple(map(int, input().split())) for _ in range(n)]
mem = {}
def solve(i, j, cur_d):
    if j <= i:
        return 0
    if (res := mem.get((i, j, cur_d))) is not None:
        return res
    res = (j-i) * cur_d
    for s, e, p, d in plans:
        if d < cur_d and e > i and s < j:
            a = max(i, s)
            b = min(j, e)
            res = min(res, solve(i, a, cur_d) + p + solve(a, b, d) + solve(b, j, cur_d))
    mem[(i, j, cur_d)] = res
    return res
print(solve(0, 300, 2**30))
