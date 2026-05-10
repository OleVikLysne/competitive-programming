A, s = input().split("=")
B = [int(x) for x in A]
s = int(s)
n = len(B)

next = [0]*n
j = 1
for i in range(n):
    if j == i:
        j += 1
    while j < n and B[j] == 0:
        j += 1
    next[i] = j if B[i] == 0 else i+1

pred_row = [[-1]*(n+1) for _ in range(s+1)]
pred_col = [[-1]*(n+1) for _ in range(s+1)]
count = [[2**30]*(n+1) for _ in range(s+1)]
pred_row[s][0] = -2
count[s][0] = 0
for i in range(s, -1, -1):
    for j in range(n):
        if pred_row[i][j] == -1: continue
        x = 0
        for k in range(next[j], min(n+1, next[j]+5)):
            x = x * 10 + B[k-1]
            l = i - x
            if l < 0: break
            if count[i][j] + 1 < count[l][k]:
                count[l][k] = count[i][j] + 1
                pred_row[l][k] = i
                pred_col[l][k] = j

stack = []
i = 0
j = n
while i != s:
    k = pred_row[i][j]
    l = pred_col[i][j]
    stack.append(A[l:j])
    i, j = k, l
print("+".join(reversed(stack))+f"={s}")
