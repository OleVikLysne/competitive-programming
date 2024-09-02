import sys; input=sys.stdin.readline; print=sys.stdout.write

r = int(input())
c = int(input())
u = int(input())
grid = [[0]*c for _ in range(r)]
for i in range(r):
    inp = input()
    for j in range(c):
        char = inp[j]
        if char == "#":
            grid[i][j] = 1
        elif char == "S":
            start = (i, j)

def valid_moves(i, j):
    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if 0 <= x < r and 0 <= y < c:
            yield x, y

def dfs(i, j):
    l = 1
    stack = [(i, j)]
    while stack:
        for x, y in valid_moves(*stack.pop()):
            if visited[x][y] or not grid[x][y]:
                continue
            l += 1
            stack.append((x, y))
            visited[x][y] = True
    return l

visited = [[False]*c for _ in range(r)]
i, j = start
visited[i][j] = True
land = dfs(i, j)
print(f"{land} ")
for _ in range(u):
    i, j = (int(x)-1 for x in input().split())
    grid[i][j] = 1
    for x, y in valid_moves(i, j):
        if visited[x][y]:
            visited[i][j] = True
            land += dfs(i, j)
            break
    print(f"{land} ")
