import sys

m = {
    "+": lambda x, y: x+y,
    "*": lambda x, y: x*y
}

ROWS = 4

grid = [[int(x) for x in next(sys.stdin).split()] for _ in range(ROWS)]
COLS = len(grid[0])

ops = next(sys.stdin).split()

res = 0
for j in range(COLS):
    x = 1 if ops[j] == "*" else 0
    for i in range(ROWS):
        x = m[ops[j]](x, grid[i][j])
    res += x

print(res)