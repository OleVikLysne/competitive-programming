import sys; input = sys.stdin.readline

n, m = map(int, input().split())
grid = [input().rstrip() for _ in range(n)]

def count(grid, char):
    c = 0
    for row in grid:
        for elem in row:
            if elem == char:
                c += 1
    return c

def gen():
    for i in range(n):
        yield (i, 0, 0, 1)
        yield (0, i, 1, 0)

    for i in range(n-m):
        yield (i, 0, 1, 1)

    for j in range(1, n-m):
        yield (0, j, 1, 1)

    for i in range(m, n):
        yield (i, 0, -1, 1)

    for j in range(n-m):
        yield (n - 1, j, -1, 1)


def get_win_list(grid, char):
    win_list = []
    for i, j, di, dj in gen():
        found = []
        while 0 <= i < n and 0 <= j < n:
            if grid[i][j] != char:
                if len(found) >= m:
                    win_list.append(found)
                found = []
            else:
                found.append((i, j))
            i += di
            j += dj

        if len(found) >= m:
            win_list.append(found)
    return win_list

def dist(i, j, x, y):
    return max(abs(i-x), abs(j-y))

def check(grid, char):
    win_list = get_win_list(grid, char)
    if len(win_list) == 0:
        return 0
    for found in win_list:
        if len(found) >= 2*m:
            return 2

    if len(win_list) == 1:
        return 1

    s = set(win_list[0])
    for k in range(1, len(win_list)):
        s = s.intersection(win_list[k])
    if len(s) == 0:
        return 2

    i, j = s.pop()
    for x in win_list:
        for l in (0, -1):
            if dist(i, j, *x[l]) >= m:
                return 2
    return 1


def error(o_wins, x_wins, diff):
    if o_wins == 2 or x_wins == 2:
        return True
    if x_wins == 1 and o_wins == 1:
        return True
    if not 0 <= diff <= 1:
        return True
    if x_wins == 1 and diff != 1:
        return True
    if o_wins == 1 and diff != 0:
        return True

    return False

o_wins = check(grid, "O")
x_wins = check(grid, "X")
if error(o_wins, x_wins, count(grid, "X")-count(grid, "O")):
    print("ERROR")
elif x_wins == 1:
    print("X WINS")
elif o_wins == 1:
    print("O WINS")
elif count(grid, ".") == 0:
    print("DRAW")
else:
    print("IN PROGRESS")
