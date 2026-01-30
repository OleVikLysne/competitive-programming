import sys; input=sys.stdin.readline

def eval(mi):
    mini = float("inf")
    maxi = -float("inf")
    for t, v in A:
        x = (mi-t)*v
        maxi = max(maxi, x)
        mini = min(mini, x)
    return maxi-mini

n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]
lo, hi = A[max(range(n), key = lambda x: A[x][0])][0], 2**30
while hi-lo > 1e-7:
    m1 = lo + (hi-lo) / 2.1
    m2 = hi - (hi-lo) / 2.1
    if eval(m1) <= eval(m2):
        hi = m2
    else:
        lo = m1

print(eval(hi))