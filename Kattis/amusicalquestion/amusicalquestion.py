c, n = map(int, input().split())
dp = [[False]*(c+1) for _ in range(c+1)]
dp[0][0] = True
for val in map(int, input().split()):
    for i in range(c, -1, -1):
        for j in range(c, -1, -1):
            if not dp[i][j]:
                continue
            if i+val <= c:
                dp[i+val][j] = True
            if j+val <= c:
                dp[i][j+val] = True
a, b = 0, 0
for i in range(c, -1, -1):
    for j in range(i, -1, -1):
        if i+j < a+b:
            break
        if dp[i][j]:
            a, b = i, j
print(a, b)