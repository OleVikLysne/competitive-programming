import sys;input=sys.stdin.readline

def sieve(n):
    n += 1
    prime = [True]*n
    prime[0] = prime[1] = False
    l = []
    for i in range(2, n):
        if not prime[i]:
            continue
        l.append(i)
        for j in range(i*2, n, i):
            prime[j] = False
    return l

primes = sieve(300)

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = (int(x)-1 for x in input().split())
    g[u].append(v)
    g[v].append(u)

parent = [-1]*n
def remove_parent(v, par):
    if par != -1:
        parent[v] = par
        g[v].remove(par)
    for u in g[v]:
        remove_parent(u, v)
remove_parent(0, -1)

labels = [0]*n
visited = [False]*n
labels[0] = 1
visited[0] = True
longest = []
def dfs(v, p):
    global longest
    if not visited[v]:
        p.append(v)
    if not g[v]:
        if len(p) > len(longest):
            longest = [x for x in p]
    else:
        for u in g[v]:
            dfs(u, p)
    if not visited[v]:
        p.pop()

for i in range(n):
    longest.clear()
    dfs(0, [])
    if not longest:
        break
    for v in longest:
        labels[v] = labels[parent[v]] * primes[i]
        visited[v] = True
print(*labels)