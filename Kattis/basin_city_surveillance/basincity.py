import sys; input=sys.stdin.readline

k = int(input())
n = int(input())
if n >= 5*k:
    print("possible")
    exit()

adj_mask = [0]*n
g = [[] for _ in range(n)]
for i in range(n):
    adj_mask[i] |= 1 << i
    for j in map(lambda x: int(x)-1, input().split()[1:]):
        g[i].append(j)
        adj_mask[i] |= 1 << j

non_adj_n = [[] for _ in range(n)]
for v in range(n):
    for i in range(len(g[v])):
        for j in range(i+1, len(g[v])):
            u, w = g[v][i], g[v][j]
            if adj_mask[u] & 1 << w:
                continue
            non_adj_n[v].append((u, w))

def search(v=0, mask=0, c=0):
    if c >= k:
        return True
    if v == n:
        return False
    if adj_mask[v] & mask:
        return search(v+1, mask, c)
    
    if search(v+1, mask | 1 << v, c+1):
        return True
    
    for u, w in non_adj_n[v]:
        if adj_mask[u] & mask or adj_mask[w] & mask:
            continue
        if search(v+1, mask | 1 << u | 1 << w, c+2):
            return True
    
    return False

if search():
    print("possible")
else:
    print("impossible")