from sys import stdin

n, l = map(int, stdin.readline().split())
status = [-1 for _ in range(n)]
name_to_idx = {}
verdict = "0"

roots = []
for _ in range(n):
    p, s = stdin.readline().split()
    i = len(name_to_idx)
    name_to_idx[p] = len(name_to_idx)
    if s == "u":
        s = 0
    elif s == "m":
        s = 1
        roots.append(i)
    else:
        s = 2
    status[i] = s

g = [-1 for _ in range(n)]


for _ in range(l):
    p1, arrow, p2 = stdin.readline().split()
    i, j = name_to_idx[p1], name_to_idx[p2]
    g[i] = j
    if status[i] == 1 and status[j] == 0:
        print(1)
        exit()
    if (status[i] == 1 and status[j] == 2) or (status[i] == 2 and status[j] == 0) or (status[i] == 2 and status[j] == 2):
        verdict = "?"


visited = [False for _ in range(n)]
for i in roots:
    if not visited[i]:
        visited[i] = True
        ptr = i
        m = False
        while g[ptr] != -1 and not visited[g[ptr]]:
            if status[ptr] == 1:
                m = True
            ptr = g[ptr]
            visited[ptr] = True
            if status[ptr] == 0 and m:
                print(1)
                exit()
print(verdict)