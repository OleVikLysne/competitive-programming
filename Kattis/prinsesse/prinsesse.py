m, n, s = map(int, input().split())
dp = [[-1]*(m+1) for _ in range(n+1)]
def search(n, m):
    if m == 1:
        return True
    if n <= 0:
        return False
    if dp[n][m] != -1:
        return dp[n][m]
    dp[n][m] = 0
    for k in range(1, m//2+1):
        a, b = search(n-s-1, k), search(n-1, m-k)
        if not (a or b):
            break
        if a and b:
            dp[n][m] = k
            break
    return dp[n][m]

l = [x for x in range(m)]
while m > 1:
    to_try = [l.pop() for _ in range(search(n, m))]
    print("?", *to_try)
    if int(input()):
        l = to_try
        n -= s
    n -= 1
    m = len(l)

print("!", l[0])