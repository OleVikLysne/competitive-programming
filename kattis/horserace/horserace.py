import sys; input=sys.stdin.readline
import bisect

n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

T = [0]*(n+1)
for i in range(n):
    j = bisect.bisect_right(B, A[i])
    l = (-i) % n
    r = (-i+j) % n
    T[l] += 1
    T[r] -= 1
    if l >= r:
        T[0] += 1

c = 0
res = 0
for i in range(n):
    c += T[i]
    if c == n:
        res += 1
print(res)