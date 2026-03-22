a, b, c = map(int, input().split())

mem = [[[[-1]*9 for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]
def solve(a, b, c, d):
    if a < 0 or b < 0 or c < 0:
        return -2**60
    if d == 0:
        return 0
    if mem[a][b][c][d] != -1:
        return mem[a][b][c][d]
    res = max(
        2 + solve(a-1, b, c, abs(d-2)),
        4 + solve(a, b-1, c, abs(d-4)),
        8 + solve(a, b, c-1, abs(d-8))
    )
    mem[a][b][c][d] = res
    return res


res = max(
        2 + solve(a-1, b, c, 2),
        4 + solve(a, b-1, c, 4),
        8 + solve(a, b, c-1, 8),
        0
    )
print(res // 2)