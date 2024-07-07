from sys import stdin, stdout

def dfs(v, mem):
    if v == 400:
        return 1
    if v == 401:
        return 0
    if mem[v] != -1:
        return mem[v]
    s = 0
    for u in g[v]:
        s += dfs(u, mem)
    mem[v] = s
    return s
    

t = int(stdin.readline())
for _ in range(t):
    s = int(stdin.readline())
    g = [[] for _ in range(402)]
    for _ in range(s):
        l = stdin.readline().split()
        if len(l) == 2:
            node, outcome = int(l[0])-1, 400 if l[1][0] == "f" else 401
            g[node].append(outcome)
        else:
            a, b, c, d = [int(x)-1 for x in l]
            for x in (b, c, d):
                g[a].append(x)
    
    mem = [-1]*400
    stdout.write(str(dfs(0, mem))+"\n")
            
