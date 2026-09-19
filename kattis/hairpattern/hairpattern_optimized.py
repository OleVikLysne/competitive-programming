n, m = map(int, input().split())

gr = [0]*n
gc = [0]*n
for i in range(n):
    for j, x in enumerate(input()):
        if x == "W":
            gr[i] |= 1 << j
            gc[j] |= 1 << i

tr = [0]*n
tc = [0]*n
for i in range(n):
    for j, x in enumerate(input()):
        if x == "W":
            tr[i] |= 1 << j
            tc[j] |= 1 << i

c = n+m
dp = [-1]*(1 << c)
dp[0] = n * m - sum((gr[i] ^ tr[i]).bit_count() for i in range(n))
for mask in range(1 << c):
    for k in range(c):
        if mask & 1 << k: continue
        if k < n:
            w = (tr[k] ^ ((mask >> n) & tr[k])).bit_count()
            b = m - (tr[k] | (mask >> n)).bit_count()
            l = m - ((gr[k] ^ tr[k]) | (mask >> n)).bit_count()
        else:
            w = (tc[k-n] ^ (mask & tc[k-n])).bit_count()
            b = n - ((tc[k-n] | mask) & ((1 << n)-1)).bit_count()
            l = n - (((gc[k-n] ^ tc[k-n]) | mask) & ((1 << n)-1)).bit_count()

        dp[mask | (1 << k)] = max(
            dp[mask | (1 << k)],
            dp[mask] + max(w, b) - l
        )
print(max(dp))