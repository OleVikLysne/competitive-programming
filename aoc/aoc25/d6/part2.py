import sys

m = {
    "+": lambda x, y: x+y,
    "*": lambda x, y: x*y
}

ROWS = 4

grid = [next(sys.stdin).rstrip("\n") for _ in range(ROWS)]
COLS = len(grid[0])
ops = next(sys.stdin)

def add():
    x = 1 if op == "*" else 0
    for y in nums:
        x = m[op](x, y)
    nums.clear()
    return x

res = 0
nums = []
op = None
for j in range(COLS):
    if ops[j] != " ":
        if op is not None:
            res += add()
        op = ops[j]

    num = "".join(grid[i][j] for i in range(ROWS) if grid[i][j] != " ")
    if num:
        nums.append(int(num))
        
res += add()
print(res)
