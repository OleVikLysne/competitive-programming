import sys; input=sys.stdin.readline

def valid_chess_knight_moves(i, j):
    for x, y in (
        (i + 2, j + 1),
        (i - 2, j + 1),
        (i + 2, j - 1),
        (i - 2, j - 1),
        (i + 1, j + 2),
        (i - 1, j + 2),
        (i + 1, j - 2),
        (i - 1, j - 2),
    ):
        if 0 <= x < rows and 0 <= y < cols:
            yield x, y

# open 0
# knight 1
# wall 2
# red_removable < 0
# red_permanent 3

rows, cols = map(int, input().split())
visited = [[False]*cols for _ in range(rows)]
searchable = [[False]*cols for _ in range(rows)]
grid = [[0]*cols for _ in range(rows)]
knights = []
for i in range(rows):
    for j, x in enumerate(input()):
        if x == "K":
            grid[i][j] = 1
            knights.append((i, j))
        elif x == "R":
            start = (i, j)
            visited[i][j] = True
        elif x == "T":
            target = (i, j)

def knight(i, j):
    return 1 <= grid[i][j] <= 2

def removable_knight(i, j):
    return grid[i][j] == 1

def removable_red(i, j):
    return grid[i][j] < 0

def permanent_red(i, j):
    return grid[i][j] == 3

def wall(i, j):
    return grid[i][j] == 2

def can_stop(i, j):
    return 0 <= grid[i][j] <= 1

full_block_knights = []
regular_knights = []
for i, j in knights:
    for x, y in valid_chess_knight_moves(i, j):
        if knight(x, y):
            full_block_knights.append((i, j))
            break
    else:
        regular_knights.append((i, j))
        
for i, j in regular_knights:
    for x, y in valid_chess_knight_moves(i, j):
        grid[x][y] -= 1

for i, j in full_block_knights:
    grid[i][j] = 2
    for x, y in valid_chess_knight_moves(i, j):
        if not knight(x, y):
            grid[x][y] = 3
            

def next_moves(i, j):
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        x, y = i, j
        while 0 <= x+dx < rows and 0 <= y+dy < cols:
            x += dx
            y += dy
            if wall(x, y): break
            if visited[x][y]: continue
            searchable[x][y] = True
            if can_stop(x, y):
                yield x, y
                break

def remove_knight(i, j):
    grid[i][j] = 0
    for x, y in valid_chess_knight_moves(i, j):
        if removable_red(x, y):
            grid[x][y] += 1
            if grid[x][y] == 0:
                yield x, y

def yes():
    print("yes")
    exit()
def no():
    print("no")
    exit()

if permanent_red(*target):
    no()

stack = [start]
while stack:
    for i, j in next_moves(*stack.pop()):
        if (i, j) == target:
            yes()
        visited[i][j] = True
        if removable_knight(i, j):
            for x, y in remove_knight(i, j):
                if not visited[x][y] and searchable[x][y]:
                    if (x, y) == target:
                        yes()
                    visited[x][y] = True
                    stack.append((x, y))
        stack.append((i, j))
no()