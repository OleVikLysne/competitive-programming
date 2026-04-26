import io, os
Ø = io.BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: next(Ø)

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

last = [0]*(k+1)
for i in range(n):
    last[arr[i]] = i

stack = []
used = [False]*(k+1)
for i in range(n):
    x = arr[i]
    if used[x]: continue
    while stack and stack[-1] > x and last[stack[-1]] > i:
        used[stack.pop()] = False
    stack.append(x)
    used[x] = True

print(" ".join(map(str, stack)))
