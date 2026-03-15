from sys import stdin, stdout



n = int(stdin.readline())
g = [[] for _ in range(n+1)]
roots = []
ancestors = [set() for _ in range(n+1)]
descendants = [0]*(n+1)

for i, x in enumerate(stdin.readline().split()):
    if x == "0":
        roots.append(i+1)
        continue
    x = int(x)
    g[x].append(i+1)


l = set()
def build_anc(v):
    s = 0
    for u in g[v]:
        ancestors[u].union(ancestors[v])
        ancestors[u].add(v) 
        s += 1
        s += build_anc(u)
    descendants[v] = s
    return s

for root in roots:
    build_anc(root)


q = int(stdin.readline())
for _ in range(q):
    stdin.read(2)
    query = set(int(x) for x in stdin.readline().split())
    mask = 0
    s = 0
    for x in query:
        if len(ancestors[x].intersection(query)) == 0:
            s += descendants[x] + 1
    stdout.write(str(s)+"\n")