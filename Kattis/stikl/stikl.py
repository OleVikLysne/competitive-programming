import sys; input=sys.stdin.readline

n, q = map(int, input().split())
tiles = [int(x) for x in input().split()]
log_n = (n-1).bit_length()
matrix = [[-1]*n for _ in range(log_n)]
stack = [0]

for i in range(1, n):
    while stack and tiles[i] >= tiles[stack[-1]]:
        matrix[0][stack.pop()] = i
    stack.append(i)

for i in range(1, log_n):
    for j in range(n):
        matrix[i][j] = matrix[i-1][matrix[i-1][j]]


for _ in range(q):
    s, d = map(int, input().split())
    s -= 1
    i = d.bit_length()-1
    while d:
        if d & 1 << i:
            s = matrix[i][s]
        d &= (1 << i) - 1
        i -= 1
    sys.stdout.write("leik lokid " if s == -1 else f"{s+1} ")
