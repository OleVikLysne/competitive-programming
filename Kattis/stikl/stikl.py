import sys; input=sys.stdin.readline

n, q = map(int, input().split())
tiles = [int(x) for x in input().split()]
log_n = (n-1).bit_length()
next = [[-1]*n for _ in range(log_n)]
stack = [0]

for i in range(1, n):
    while stack and tiles[i] >= tiles[stack[-1]]:
        next[0][stack.pop()] = i
    stack.append(i)

for i in range(1, log_n):
    for j in range(n):
        next[i][j] = next[i-1][next[i-1][j]]

for _ in range(q):
    s, d = map(int, input().split())
    s -= 1
    log_d = (d-1).bit_length()
    for i in range(log_d, -1, -1):
        if d & 1 << i:
            s = next[i][s]
    sys.stdout.write("leik lokid " if s == -1 else f"{s+1} ")
