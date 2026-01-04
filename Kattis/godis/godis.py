import sys; input=sys.stdin.readline

K = 10

n = int(input())
candies = [[0]*K for _ in range(n)]
for i in range(n):
    k, *inp = map(int, input().split())
    for j in range(0, 2*k, 2):
        t, k = inp[j], inp[j+1]
        k = -k if t < 0 else k
        candies[i][abs(t)-1] = k

res = 0
for mask in range(1 << K):
    pick = [0]*K
    for i in range(n):
        s = 0
        for j in range(K):
            if mask & 1 << j:
                s += candies[i][j]
            else:
                s -= candies[i][j]
        if s > 0:
            for j in range(K):
                pick[j] += candies[i][j]

    res = max(res, sum(map(abs, pick)))
print(res)
