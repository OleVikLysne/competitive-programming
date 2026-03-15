from sys import stdin, stdout

r, c = map(int, stdin.readline().split())


def moves(i, j):
    for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        if 0 <= x < r and 0 <= y < c and grid[i][j] == grid[x][y]:
            yield x, y


grid = [[int(x) for x in stdin.readline().rstrip()] for _ in range(r)]


def reachable(i, j):
    stack = [(i, j)]
    visited = set([(i, j)])
    while stack:
        for pos in moves(*stack.pop()):
            if pos in visited:
                continue
            visited.add(pos)
            stack.append(pos)
    return visited


components = []
n = int(stdin.readline())
for _ in range(n):
    i, j, x, y = [int(x)-1 for x in stdin.readline().split()]
    for comp in components:
        if (i, j) in comp:
            if (x, y) in comp:
                stdout.write("binary\n" if grid[i][j] == 0 else "decimal\n")
            else:
                stdout.write("neither\n")
            break
    else:
        reachable_nodes = reachable(i, j)
        if (x, y) in reachable_nodes:
            stdout.write("binary\n" if grid[i][j] == 0 else "decimal\n")
        else:
            stdout.write("neither\n")
        components.append(reachable_nodes)
