import io, os
Ø = io.BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: next(Ø)

MOD = 10**9+7

cols, rows, n = map(int, input().split())

R = [False]*rows
C = [False]*cols

for _ in range(n):
    r, m = map(int, input().split())
    if r < rows:
        R[r] = True
    if m-r < cols:
        C[m-r] = True

if (rows <= cols and C[cols-rows]) or (cols < rows and R[rows-cols]):
    print(0)
    exit()

res = [[0]*cols for _ in range(rows)]
res[-1][-1] = 1
for i in range(rows-1, -1, -1):
    for j in range(cols-1, -1, -1):
        if (i <= j and C[j-i]) or (j < i and R[i-j]):
            continue
        if i+1 < rows:
            res[i][j] += res[i+1][j]
        if j+1 < cols:
            res[i][j] += res[i][j+1]
        res[i][j] %= MOD
print(res[0][0])
