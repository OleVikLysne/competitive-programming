from sys import stdin, stdout

n, k = map(int, stdin.readline().split())

g = [[] for _ in range(n)]
roots = set(range(n))
leaves = set(range(n))
for _ in range(k):
    i, j = [int(x) for x in stdin.readline().split()]
    g[i].append(j)
    if j in roots:
        roots.remove(j)
    if i in leaves:
        leaves.remove(i)


distance = [0]*n
def distance_to_leaf(v):
    if distance[v] != 0:
        return distance[v]
    if v == leaf:
        return 0
    dist = 0
    for u in g[v]:
        dist = max(dist, 1 + distance_to_leaf(u))
    distance[v] = dist
    return dist

def argmax(l):
    w = l[0]
    for u in l:
        if distance[u] > distance[w]:
            w = u
    return w

if len(roots) == 1 and len(leaves) == 1:
    leaf = leaves.__iter__().__next__()
    root = roots.__iter__().__next__()
    distance_to_leaf(root)
    v = root
    stack = [v]
    while v != leaf:
        v = argmax(g[v])
        stack.append(v)
    if len(stack) == n:
        for x in stack:
            stdout.write(str(x) + " ")
        exit()

stdout.write("back to the lab")
