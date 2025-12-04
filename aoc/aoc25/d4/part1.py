import sys

def valid_moves(i, j):
    l = []
    for x, y in (
        (i + 1, j),
        (i - 1, j),
        (i, j + 1),
        (i, j - 1),
        (i + 1, j + 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i - 1, j - 1),
    ):
        if 0 <= x < rows and 0 <= y < cols:
            l.append((x, y))
    return l

grid = [[c for c in line.rstrip()] for line in sys.stdin]
rows = len(grid)
cols = len(grid[0])

s = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "@":
            if sum(grid[x][y] == "@" for x, y in valid_moves(i, j)) < 4:
                s += 1
print(s)