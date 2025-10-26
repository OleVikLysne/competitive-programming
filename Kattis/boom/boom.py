import io, os
Ø = io.BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: next(Ø).decode()

n, r = map(int, input().split())
grid = [[c for c in input().rstrip()] for _ in range(n)]

def valid(i, j):
    return 0 <= i < n and 0 <= j < n and grid[i][j] != "#"


def in_range(i, j, filter = lambda *_: True):
    l = []
    for k in range(i+1, i+1+r):
        if not valid(k, j):
            break
        if filter(k, j):
            l.append((k, j))

    for k in range(i-1, i-1-r, -1):
        if not valid(k, j):
            break
        if filter(k, j):
            l.append((k, j))

    for k in range(j+1, j+1+r):
        if not valid(i, k):
            break
        if filter(i, k):
            l.append((i, k))


    for k in range(j-1, j-1-r, -1):
        if not valid(i, k):
            break
        if filter(i, k):
            l.append((i, k))
    return l


stumps = []
stump_ids = [[-1]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == "S":
            stump_ids[i][j] = len(stumps)
            stumps.append((i, j))

def mark_reachable_bombs(i, j, comp, comp_id):
    comp[i][j] = comp_id
    stack = [(i, j)]
    found_stumps = set()
    while stack:
        i, j = stack.pop()
        for x, y in in_range(i, j, filter = lambda x, y: grid[x][y] == "S" or (grid[x][y] == "*" and comp[x][y] == -1)):
            if grid[x][y] == "S":
                found_stumps.add(stump_ids[x][y])
            else:
                comp[x][y] = comp_id
                stack.append((x, y))
    return found_stumps


comp = [[-1]*n for _ in range(n)]
comp_to_stump = []
for i in range(n):
    for j in range(n):
        if grid[i][j] != "*" or comp[i][j] != -1:
            continue
        comp_id = len(comp_to_stump)
        found_stumps = mark_reachable_bombs(i, j, comp, comp_id)
        comp_to_stump.append(list(found_stumps))


comp_left = [[-1]*n for _ in range(n)]
for i in range(n):
    prev = -1
    for j in range(n):
        if comp[i][j] != -1:
            prev = j
        if grid[i][j] == "#":
            prev = -1
        if prev != -1 and grid[i][j] == "." and j-prev <= r:
            comp_left[i][j] = comp[i][prev]

comp_right = [[-1]*n for _ in range(n)]
for i in range(n):
    prev = -1
    for j in range(n-1, -1, -1):
        if comp[i][j] != -1:
            prev = j
        if grid[i][j] == "#":
            prev = -1
        if prev != -1 and grid[i][j] == "." and prev-j <= r:
            comp_right[i][j] = comp[i][prev]

comp_up = [[-1]*n for _ in range(n)]
for j in range(n):
    prev = -1
    for i in range(n):
        if comp[i][j] != -1:
            prev = i
        if grid[i][j] == "#":
            prev = -1
        if prev != -1 and grid[i][j] == "." and i-prev <= r:
            comp_up[i][j] = comp[prev][j]

comp_down = [[-1]*n for _ in range(n)]
for j in range(n):
    prev = -1
    for i in range(n-1, -1, -1):
        if comp[i][j] != -1:
            prev = i
        if grid[i][j] == "#":
            prev = -1
        if prev != -1 and grid[i][j] == "." and prev-i <= r:
            comp_down[i][j] = comp[prev][j]


def remove(count, comp, m):
    for x in comp_to_stump[comp]:
        count[x] -= 1
        if count[x] == 0:
            m += 1
    return m


def add(count, comp, m):
    for x in comp_to_stump[comp]:
        if count[x] == 0:
            m -= 1
        count[x] += 1
    return m


nearest_comp = [comp_left, comp_right, comp_up, comp_down]
cur_comps = set()
S = len(stumps)
count = [0]*S
m = S
total = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != ".":
            continue
        new_comps = {x for k in range(4) if (x := nearest_comp[k][i][j]) != -1}
        for c in cur_comps:
            if c not in new_comps:
                m = remove(count, c, m)
        for c in new_comps:
            if c not in cur_comps:
                m = add(count, c, m)
        cur_comps = new_comps

        extra = 0
        if m:
            extra += len(in_range(i, j, filter = lambda x, y: stump_ids[x][y] != -1 and count[stump_ids[x][y]] == 0))
        if not m-extra:
            total += 1
print(total)
