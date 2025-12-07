import sys

grid = [[c for c in line.rstrip()] for line in sys.stdin]
rows = len(grid)
cols = len(grid[0])

sj = grid[0].index("S")
mem = [[-1]*cols for _ in range(rows)]
def solve(i, j):
    if i == rows:
        return 1
    if mem[i][j] != -1:
        return mem[i][j]
    if grid[i][j] == "^":
        res = solve(i+1, j+1) + solve(i+1, j-1)
    else:
        res = solve(i+1, j)
    mem[i][j] = res
    return res

print(solve(1, sj))
