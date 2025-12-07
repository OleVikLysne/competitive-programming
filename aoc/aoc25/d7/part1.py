import sys

grid = [[c for c in line.rstrip()] for line in sys.stdin]
rows = len(grid)
cols = len(grid[0])

sj = grid[0].index("S")
idxs = {sj}
splits = 0
for i in range(1, rows):
    next_idxs = set()
    for j in idxs:
        if grid[i][j] == "^":
            next_idxs.add(j-1)
            next_idxs.add(j+1)
            splits += 1
        else:
            next_idxs.add(j)
    idxs = next_idxs
print(splits)
