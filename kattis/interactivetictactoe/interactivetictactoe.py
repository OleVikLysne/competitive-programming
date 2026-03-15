input()
mem = {}

def check_win(grid, char):
    for i in range(3):
        if all(grid[i][j] == char for j in range(3)):
            return True

    for j in range(3):
        if all(grid[i][j] == char for i in range(3)):
            return True
    
    if all(grid[i][i] == char for i in range(3)):
        return True
    
    if all(grid[2-i][i] == char for i in range(3)):
        return True
    
    return False

def check_draw(grid):
    return not any("." in row for row in grid)

def dp(grid, t):
    tup = tuple(tuple(row) for row in grid)
    if (res := mem.get(tup)) is not None:
        return res
    
    prev_char = "o" if t == 0 else "x"
    if check_win(grid, prev_char):
        res = (None, prev_char)
    
    elif check_draw(grid):
        res = (None, ".")
    else:
        char = "x" if t == 0 else "o"
        res = None, prev_char
        for i in range(3):
            for j in range(3):
                if grid[i][j] == ".":
                    grid[i][j] = char
                    _, outcome = dp(grid, (t+1)%2)
                    if res[0] is None or outcome == char or (outcome == "." and res[1] == prev_char):
                        res = ((i, j), outcome)
                    grid[i][j] = "."
    mem[tup] = res
    return res


while True:
    grid = [[c for c in input().lstrip(" ")] for _ in range(3)]
    if check_draw(grid) or check_win(grid, "x"):
        break
    (i, j), _ = dp(grid, 0)
    grid[i][j] = "x"
    for row in grid:
        print("".join(row))
    
    if check_draw(grid) or check_win(grid, "x"):
        break
