from sys import stdin, stdout
from math import comb
form = "Game {} -- {} : {}\n"
h = int(stdin.readline())
buf = [None]*h
for g in range(h):
    n = int(stdin.readline())
    tiles = tuple(map(int, stdin.readline().split()))
    k, t = map(int, stdin.readline().split())
    if k >= 15:
        s = sum(tiles)
        if (t+1)*(k+1) > (s-t+1)*(n-k+1):
            k = n - k
            t = s - t
    t += 1
    indices = ([0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
    dp = [0]*(k+1)*t
    dp[0] = 1
    b = k-n
    for v in tiles:
        for i in range(k, 0 if b <= 0 else b, -1):
            for j in indices[i-1]:
                if j+v < t:
                    if dp[i*t+j+v] == 0:
                        indices[i].append(j+v)
                    dp[i*t+j+v] += dp[(i-1)*t+j]
        b += 1
    w = dp[-1]
    buf[g] = (w, comb(n, k)-w)
stdout.write("".join(form.format(i, *args) for i, args in enumerate(buf, 1)))