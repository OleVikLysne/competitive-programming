import sys; input=sys.stdin.readline

n, k = map(int, input().split())
n -= 1
m = [[0]*n for _ in range(k)]
base = [ord(x)-65 for x in input().rstrip()]
for j in range(n):
    for i, x in enumerate(input().rstrip()):
        m[ord(x)-65][j] = i

res = [1]*k
for l in range(k):
    for i in range(l+1, k):
        for j in range(n):
            if m[base[i]][j] <= m[base[l]][j]:
                break
        else:
            res[i] = max(res[i], res[l]+1)
print(max(res))
